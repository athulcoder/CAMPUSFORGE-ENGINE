# app/models/project.py
from app.extensions import db

class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.BigInteger, primary_key=True)
    resume_id = db.Column(
        db.BigInteger, db.ForeignKey("resumes.id"), nullable=False
    )

    project_title = db.Column(db.String(255))
    description = db.Column(db.Text)
    tech_stack = db.Column(db.String(255))
    github_repo = db.Column(db.String(255))