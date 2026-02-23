from flask import Flask
from .config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # INIT EXTENSIONS
    db.init_app(app)
    migrate.init_app(app, db)  # 👈 THIS ENABLES "flask db"

    # IMPORT MODELS (IMPORTANT FOR MIGRATIONS)
    from .models import (
        Recruiter,
        Candidate,
        Resume,
        Skill,
        ResumeSkill,
        Education,
        Experience,
        Project
    )

  

    return app