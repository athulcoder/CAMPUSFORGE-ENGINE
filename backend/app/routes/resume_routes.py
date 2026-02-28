from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

import uuid
from backend.services.candidate_cache import update_candidate_status
from backend.db.session import SessionLocal
from backend.models.resume import Resume, UploadStatus, ProcessingStatus,SelectionStatus
from backend.services.minio_service import upload_resume_minio
from backend.services.redis_service import enqueue_resume_job
from backend.app.websockets.redis_listener import start_redis_listener
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
    upload_resume_minio(
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
    start_redis_listener(resume_id)
    return jsonify({
        "resume_id": resume_id,
        "upload_status": upload_status,
        "processing_status": processing_status
    }), 201




@resume_bp.route('/<resume_id>/approve', methods=['POST'])
@jwt_required()
def approve_resume(resume_id):
    data = request.get_json(silent=True) or {}
    review_note = data.get("review_note")
    recruiter_id = get_jwt_identity()

    db = SessionLocal()
    try:
        resume = db.query(Resume).filter_by(id=resume_id).first()

        if not resume:
            return jsonify({"error": "Resume not found"}), 404

        if resume.recruiter_id != recruiter_id:
            return jsonify({"error": "Forbidden"}), 403

        if resume.selection_status != SelectionStatus.PENDING:
            return jsonify({"error": "Resume already reviewed"}), 400

        old_status = resume.selection_status.value

        resume.selection_status = SelectionStatus.ACCEPTED
        resume.review_note = review_note

        db.commit()

        update_candidate_status(
            candidate_id=resume.id,
            old_status=old_status,
            new_status=resume.selection_status.value,
            role=resume.maching_role,
            score=resume.resume_score
        )

        return jsonify({
            "resume_id": resume.id,
            "selection_status": resume.selection_status.value,
            "message": "Resume approved"
        }), 200

    finally:
        db.close()

@resume_bp.route('/<resume_id>/reject', methods=['POST'])
@jwt_required()
def reject_resume(resume_id):
    data = request.get_json(silent=True) or {}
    review_note = data.get("review_note")
    recruiter_id = get_jwt_identity()

    db = SessionLocal()
    try:
        resume = db.query(Resume).filter_by(id=resume_id).first()

        if not resume:
            return jsonify({"error": "Resume not found"}), 404

        if resume.recruiter_id != recruiter_id:
            return jsonify({"error": "Forbidden"}), 403

        if resume.selection_status != SelectionStatus.PENDING:
            return jsonify({"error": "Resume already reviewed"}), 400

        old_status = resume.selection_status.value

        resume.selection_status = SelectionStatus.REJECTED
        resume.review_note = review_note

        db.commit()

        update_candidate_status(
            candidate_id=resume.id,
            old_status=old_status,
            new_status=resume.selection_status.value,
            role=resume.maching_role,
            score=resume.resume_score
        )

        return jsonify({
            "resume_id": resume.id,
            "selection_status": resume.selection_status.value,
            "message": "Resume rejected"
        }), 200

    finally:
        db.close()