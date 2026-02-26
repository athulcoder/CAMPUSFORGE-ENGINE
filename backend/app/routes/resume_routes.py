from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

import uuid

from backend.db.session import SessionLocal
from backend.models.resume import Resume, UploadStatus, ProcessingStatus
from backend.services.minio_service import upload_resume
from backend.services.redis_service import enqueue_resume_job

from backend.app.utils.file_validation import validate_file

resume_bp = Blueprint(
    "resume",
    __name__,
    url_prefix="/api/resume"
)

@resume_bp.post("/upload")
@jwt_required()
def upload_resume():
    file = request.files.get("file")
    recruiter_id = get_jwt_identity()

    if not file:
        return jsonify({"error": "No file provided"}), 400

    validate_file(file)

    resume_id = str(uuid.uuid4())
    ext = file.filename.rsplit(".", 1)[1].lower()
    object_name = f"{resume_id}.{ext}"

    file_bytes = file.read()

    # 1️⃣ Upload to MinIO
    upload_resume(
        object_name=object_name,
        data=file_bytes,
        content_type=file.mimetype
    )

    db = SessionLocal()

    resume = Resume(
        id=resume_id,
        recruiter_id=recruiter_id,
        bucket="resumes",
        object_name=object_name,
        upload_status=UploadStatus.UPLOADED,
        processing_status=ProcessingStatus.QUEUED
    )

    # ✅ Capture enum values BEFORE commit/close
    upload_status = resume.upload_status.value
    processing_status = resume.processing_status.value

    db.add(resume)
    db.commit()
    db.close()

    # 3️⃣ Enqueue Redis job (async, non-blocking)
    enqueue_resume_job({
        "resume_id": resume_id,
        "bucket": "resumes",
        "object_name": object_name
    })

    return jsonify({
        "resume_id": resume_id,
        "upload_status": upload_status,
        "processing_status": processing_status
    }), 201