# models/education.py
from sqlalchemy import Column , String, ForeignKey,Float,Integer
from sqlalchemy.orm import relationship
from backend.db.base import Base
import uuid
class Education(Base):
    __tablename__ = "educations"

    id = Column(
        String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )
    resume_id = Column(String(36), ForeignKey("resumes.id"))

    degree = Column(String(255))
    institution = Column(String(255))
    cgpa = Column(Float)
    start_year = Column(Integer)
    end_year = Column(Integer)