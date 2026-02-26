from flask import Flask
from .config import Config
from .extensions import jwt
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(
        app,
        supports_credentials=True,
        origins=[
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ],
    )

    jwt.init_app(app)

    # ✅ IMPORTANT: import models ONCE to register metadata
    import backend.models  

    # Register blueprints
    from backend.app.routes.auth_routes import auth_bp
    from backend.app.routes.recruter_routes import recruiter_bp
    from backend.app.routes.resume_routes import resume_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(recruiter_bp)
    app.register_blueprint(resume_bp)

    return app