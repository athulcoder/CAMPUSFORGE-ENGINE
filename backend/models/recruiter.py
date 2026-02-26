# app/models/recruiter.py
from sqlalchemy import Column , String
from sqlalchemy.orm import relationship
from backend.db.base import Base
import uuid
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
ph = PasswordHasher()
class Recruiter(Base):
    __tablename__ = "recruiters"

    id = Column(
        String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)

    resumes = relationship("Resume", back_populates="recruiter")


    def set_password(self, passw:str):
        self.password_hash = ph.hash(passw)
        print(self.password_hash)

    def check_password(self, password: str) -> bool:
        try:
            return ph.verify(self.password_hash, password)
        except VerifyMismatchError:
            return False
    def get_recruiter(self):
        return {
            "id":self.id,
            "email":self.email,
            "name":self.name
        }