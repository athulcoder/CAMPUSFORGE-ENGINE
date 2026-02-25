# app/models/experience.py
from app.extensions import db
import uuid
class Experience(db.Model):
    __tablename__ = "experiences"

    id = db.Column(
        db.String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )
    resume_id = db.Column(db.String(36), db.ForeignKey("resumes.id"))

    job_title = db.Column(db.String(255))
    company = db.Column(db.String(255))
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)