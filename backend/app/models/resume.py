# app/models/resume.py
from app.extensions import db

class Resume(db.Model):
    __tablename__ = "resumes"

    id = db.Column(db.BigInteger, primary_key=True)

    recruiter_id = db.Column(
        db.BigInteger, db.ForeignKey("recruiters.id"), nullable=False
    )
    candidate_id = db.Column(
        db.BigInteger, db.ForeignKey("candidates.id"), nullable=False
    )

    raw_text = db.Column(db.Text)
    processing_status = db.Column(db.String(50), default="PENDING")
    resume_score = db.Column(db.Float)

    skills = db.relationship("ResumeSkill", backref="resume", cascade="all, delete")
    educations = db.relationship("Education", backref="resume", cascade="all, delete")
    experiences = db.relationship("Experience", backref="resume", cascade="all, delete")
    projects = db.relationship("Project", backref="resume", cascade="all, delete")