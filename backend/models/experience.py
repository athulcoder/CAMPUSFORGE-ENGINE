# models/experience.py
from sqlalchemy import Column , String, ForeignKey,Text,Date
from sqlalchemy.orm import relationship
from backend.db.base import Base
import uuid
class Experience(Base):
    __tablename__ = "experiences"

    id = Column(
        String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )
    resume_id = Column(String(36), ForeignKey("resumes.id"))

    job_title = Column(String(255))
    company = Column(String(255))
    description = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)