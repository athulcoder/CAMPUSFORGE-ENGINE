from app.extensions import db
import uuid
import enum


class UploadStatus(enum.Enum):
    UPLOADING = "UPLOADING"
    UPLOADED = "UPLOADED"


class ProcessingStatus(enum.Enum):
    QUEUED = "QUEUED"
    PARSING = "PARSING"
    CALCULATING_SCORE = "CALCULATING_SCORE"
    MATCHING_JOB_ROLE = "MATCHING_JOB_ROLE"
    FINALISING = "FINALISING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


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

    bucket = db.Column(db.String(100), nullable=False)
    object_name = db.Column(db.String(255), nullable=False)

    upload_status = db.Column(
        db.Enum(UploadStatus, name="upload_status_enum"),
        nullable=False,
        default=UploadStatus.UPLOADING
    )

    processing_status = db.Column(
        db.Enum(ProcessingStatus, name="processing_status_enum"),
        nullable=True,
        default=ProcessingStatus.QUEUED,
        index=True
    )

    raw_text = db.Column(db.Text, nullable=True)
    resume_score = db.Column(db.Float, nullable=True)

    skills = db.relationship(
        "Skill",
        secondary="resume_skills",
        back_populates="resumes"
    )

    educations = db.relationship("Education", cascade="all, delete")
    experiences = db.relationship("Experience", cascade="all, delete")
    projects = db.relationship("Project", cascade="all, delete")

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )