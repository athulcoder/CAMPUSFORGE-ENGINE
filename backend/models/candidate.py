# models/candidate.py

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from db.base import Base
import uuid
class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(
        String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )
    email = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    phone = Column(String(20))
    location = Column(String(255))

    resumes = relationship("Resume", back_populates="candidate")