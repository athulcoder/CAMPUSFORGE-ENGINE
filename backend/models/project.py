# models/project.py
from sqlalchemy import Column , String, ForeignKey,Float,Integer
from sqlalchemy.orm import relationship
from db.base import Base
import uuid
class Project(Base):
    __tablename__ = "projects"

    id = Column(
        String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )
    resume_id = Column(String(36), ForeignKey("resumes.id"))
    project_title = Column(String(255))
    description = Column(Text)
    tech_stack = Column(String(255))
    github_repo = Column(String(255))