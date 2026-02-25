# app/models/resume.py
from app.extensions import db
import uuid

class Resume(db.Model):
    __tablename__ = "resumes"

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    recruiter_id = db.Column(
        db.String(36),
        db.ForeignKey("recruiters.id"),
        nullable=False
    )

    candidate_id = db.Column(
        db.String(36),
        db.ForeignKey("candidates.id"),
        nullable=True
    )

    # MinIO reference
    bucket = db.Column(db.String(100), nullable=False)
    object_name = db.Column(db.String(255), nullable=False)

    # Parser output
    raw_text = db.Column(db.Text, nullable=True)
    resume_score = db.Column(db.Float, nullable=True)

    # Pipeline state
    processing_status = db.Column(
        db.String(30),
        default="UPLOADING",
        index=True
    )

    # Relationships
    skills = db.relationship(
        "Skill",
        secondary="resume_skills",
        back_populates="resumes"
    )

    educations = db.relationship("Education", cascade="all, delete")
    experiences = db.relationship("Experience", cascade="all, delete")
    projects = db.relationship("Project", cascade="all, delete")

    # Audit
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )