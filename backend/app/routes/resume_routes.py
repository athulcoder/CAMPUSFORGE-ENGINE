# app/routes/resume_routes.py
from flask import Blueprint, request, jsonify,session
import uuid
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.minio_service import upload_to_minio
from app.utils.file_validation import validate_file
from app.extensions import db
from app.models.resume import Resume
from app.services.redis_service import enqueue_resume_job
resume_bp = Blueprint("resume", __name__,url_prefix="/api/resume")

@resume_bp.post("/upload")
@jwt_required()
def upload_resume():
    file = request.files.get("file")
    recruiter_id = get_jwt_identity()

    print(recruiter_id, flush=True)
    
    resume_id = str(uuid.uuid4())
    ext = file.filename.rsplit(".", 1)[1].lower()
    object_name = f"{resume_id}.{ext}"

    file_bytes = file.read()

    upload_to_minio(object_name, file_bytes, file.mimetype)

    resume = Resume(
        id=resume_id,
        processing_status="PENDING",
        bucket="resumes",
        object_name=object_name,
        recruiter_id=recruiter_id

    )
    db.session.add(resume)
    db.session.commit()

    enqueue_resume_job({
        "resume_id": resume_id,
        "bucket": "resumes",
        "object_name": object_name,
    })

    return {
        "resume_id": resume_id,
        "status": "PENDING"
    }, 201
