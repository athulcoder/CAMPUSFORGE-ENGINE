# app/models/recruiter.py
from app.extensions import db
import uuid
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
ph = PasswordHasher()
class Recruiter(db.Model):
    __tablename__ = "recruiters"

    id = db.Column(
        db.String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    resumes = db.relationship("Resume", backref="recruiter", lazy=True)


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
            "email":self.email,
            "name":self.name
        }