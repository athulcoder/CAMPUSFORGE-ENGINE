from flask import Flask
from .config import Config
from .extensions import db, migrate,jwt
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(
        app,
        supports_credentials=True,
        origins=[
            "http://localhost:3000",
            "http://127.0.0.1:3000"
        ],
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
    from app.routes.recruter_routes import recruiter_bp
    app.register_blueprint(recruiter_bp)

    from app.routes.resume_routes import resume_bp
    app.register_blueprint(resume_bp)
    return app