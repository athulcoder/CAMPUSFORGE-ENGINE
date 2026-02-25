# app/models/resume_skill.py
from app.extensions import db
import uuid
class ResumeSkill(db.Model):
    __tablename__ = "resume_skills"

    resume_id = db.Column(
        db.String(36),
        db.ForeignKey("resumes.id"),  
        primary_key=True
    )

    skill_id = db.Column(
        db.String(36),
        db.ForeignKey("skills.id"),   
        primary_key=True
    )

    level = db.Column(db.String(50))