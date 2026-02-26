from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Enum,
    Text,
    DateTime,
    Float
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.db.base import Base
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


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    recruiter_id = Column(
        String(36),
        ForeignKey("recruiters.id", ondelete="CASCADE"),
        nullable=False
    )

    candidate_id = Column(
        String(36),
        ForeignKey("candidates.id", ondelete="SET NULL"),
        nullable=True
    )

    bucket = Column(String(100), nullable=False)
    object_name = Column(String(255), nullable=False)

    upload_status = Column(
        Enum(UploadStatus, name="upload_status_enum"),
        nullable=False,
        default=UploadStatus.UPLOADING
    )

    processing_status = Column(
        Enum(ProcessingStatus, name="processing_status_enum"),
        nullable=False,
        default=ProcessingStatus.QUEUED,
        index=True
    )

    raw_text = Column(Text)
    resume_score = Column(Float)

    skills = relationship(
        "Skill",
        secondary="resume_skills",
        back_populates="resumes",
        lazy="select"
    )

    educations = relationship(
        "Education",
        cascade="all, delete-orphan",
        lazy="select"
    )

    experiences = relationship(
        "Experience",
        cascade="all, delete-orphan",
        lazy="select"
    )

    projects = relationship(
        "Project",
        cascade="all, delete-orphan",
        lazy="select"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    recruiter = relationship(
        "Recruiter",
        back_populates="resumes"
    )

    candidate = relationship(
        "Candidate",
        back_populates="resumes",
        lazy="select"
    )

