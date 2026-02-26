# app/models/skill.py
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
class Skill(Base):
    __tablename__ = "skills"

    id = Column(
        String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )
    skill_name = Column(String(255), unique=True, nullable=False)
    category = Column(String(100))

    resumes = relationship(
        "Resume",
        secondary="resume_skills",
        back_populates="skills"
    )