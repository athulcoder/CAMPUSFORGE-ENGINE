# app/models/skill.py
from app.extensions import db

class Skill(db.Model):
    __tablename__ = "skills"

    id = db.Column(db.BigInteger, primary_key=True)
    skill_name = db.Column(db.String(255), unique=True, nullable=False)
    category = db.Column(db.String(100))

    resumes = db.relationship("ResumeSkill", backref="skill", lazy=True)