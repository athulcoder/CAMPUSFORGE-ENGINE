from flask import Flask
from .config import Config
from .extensions import db, migrate,jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    
    db.init_app(app)
    migrate.init_app(app, db)  
    jwt.init_app(app)
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

  
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)
    return app