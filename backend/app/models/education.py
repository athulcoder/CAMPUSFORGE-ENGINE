# app/models/education.py
from app.extensions import db

class Education(db.Model):
    __tablename__ = "educations"

    id = db.Column(db.BigInteger, primary_key=True)
    resume_id = db.Column(
        db.BigInteger, db.ForeignKey("resumes.id"), nullable=False
    )

    degree = db.Column(db.String(255))
    institution = db.Column(db.String(255))
    cgpa = db.Column(db.Float)
    start_year = db.Column(db.Integer)
    end_year = db.Column(db.Integer)