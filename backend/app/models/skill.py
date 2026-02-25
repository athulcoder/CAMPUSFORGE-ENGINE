# app/models/skill.py
from app.extensions import db
import uuid
class Skill(db.Model):
    __tablename__ = "skills"

    id = db.Column(
        db.String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )
    skill_name = db.Column(db.String(255), unique=True, nullable=False)
    category = db.Column(db.String(100))

    resumes = db.relationship(
        "Resume",
        secondary="resume_skills",
        back_populates="skills"
    )