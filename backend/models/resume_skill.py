# models/resume_skill.py
from sqlalchemy import Column , String,ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base
import uuid
class ResumeSkill(Base):
    __tablename__ = "resume_skills"

    resume_id = Column(
        String(36),
        ForeignKey("resumes.id"),  
        primary_key=True
    )

    skill_id = Column(
        String(36),
        ForeignKey("skills.id"),   
        primary_key=True
    )

    level = Column(String(50))