# app/models/education.py
from app.extensions import db
import uuid
class Education(db.Model):
    __tablename__ = "educations"

    id = db.Column(
        db.String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )
    resume_id = db.Column(db.String(36), db.ForeignKey("resumes.id"))

    degree = db.Column(db.String(255))
    institution = db.Column(db.String(255))
    cgpa = db.Column(db.Float)
    start_year = db.Column(db.Integer)
    end_year = db.Column(db.Integer)