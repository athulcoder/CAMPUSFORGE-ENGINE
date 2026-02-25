# app/models/resume.py
from app.extensions import db
import uuid
class Resume(db.Model):
    __tablename__ = "resumes"

    id = db.Column(
        db.String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )

    recruiter_id = db.Column(
        db.String, db.ForeignKey("recruiters.id"), nullable=False
    )
    candidate_id = db.Column(
        db.String, db.ForeignKey("candidates.id"), nullable=False
    )

    raw_text = db.Column(db.Text)
    processing_status = db.Column(db.String(50), default="PENDING")
    resume_score = db.Column(db.Float)

    skills = db.relationship(
        "Skill",
        secondary="resume_skills",
        back_populates="resumes"
    )
    educations = db.relationship("Education", backref="resume", cascade="all, delete")
    experiences = db.relationship("Experience", backref="resume", cascade="all, delete")
    projects = db.relationship("Project", backref="resume", cascade="all, delete")