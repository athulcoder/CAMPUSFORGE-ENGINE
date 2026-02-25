# app/models/candidate.py
from app.extensions import db
import uuid
class Candidate(db.Model):
    __tablename__ = "candidates"

    id = db.Column(
        db.String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )
    email = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    location = db.Column(db.String(255))

    resumes = db.relationship("Resume", backref="candidate", lazy=True)