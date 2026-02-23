# app/models/experience.py
from app.extensions import db

class Experience(db.Model):
    __tablename__ = "experiences"

    id = db.Column(db.BigInteger, primary_key=True)
    resume_id = db.Column(
        db.BigInteger, db.ForeignKey("resumes.id"), nullable=False
    )

    job_title = db.Column(db.String(255))
    company = db.Column(db.String(255))
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)