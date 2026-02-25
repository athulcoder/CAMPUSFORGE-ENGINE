# app/models/project.py
from app.extensions import db
import uuid
class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(
        db.String(36),          
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False
    )
    resume_id = db.Column(db.String(36), db.ForeignKey("resumes.id"))
    project_title = db.Column(db.String(255))
    description = db.Column(db.Text)
    tech_stack = db.Column(db.String(255))
    github_repo = db.Column(db.String(255))