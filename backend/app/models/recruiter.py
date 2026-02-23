# app/models/recruiter.py
from app.extensions import db

class Recruiter(db.Model):
    __tablename__ = "recruiters"

    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    resumes = db.relationship("Resume", backref="recruiter", lazy=True)