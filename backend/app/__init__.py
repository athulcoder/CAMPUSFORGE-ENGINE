from flask import Flask
from .config import Config
from .extensions import db, migrate,jwt
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(
        app,
        origins=[
            "http://localhost:3000",
            "http://127.0.0.1:3000"
        ],
        supports_credentials=True
    )
    
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