from flask import Flask
from .config import Config
from .extensions import jwt
from flask_cors import CORS
from backend.app.websockets.socket import socketio

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(
        app,
        supports_credentials=True,
        origins=[
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "https://campusforge-engine.vercel.app"
        ],
    )


    @app.route("/api/<path:path>", methods=["OPTIONS"])
    def options_handler(path):
        return "", 200

    jwt.init_app(app)
    socketio.init_app(app)

    # IMPORTANT: import models once
    import backend.models  
    import backend.app.websockets.events
    # Register blueprints
    from backend.app.routes.auth_routes import auth_bp
    from backend.app.routes.recruter_routes import recruiter_bp
    from backend.app.routes.resume_routes import resume_bp
    from backend.app.routes.candidate_routes import candidate_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(candidate_bp)
    app.register_blueprint(recruiter_bp)
    app.register_blueprint(resume_bp)

    return app