from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.db.session import SessionLocal
from backend.models.recruiter import Recruiter

recruiter_bp = Blueprint(
    "recruiter",
    __name__,
    url_prefix="/api/recruiter"
)


@recruiter_bp.get("/me")
@jwt_required()
def get_my_profile():
    recruiter_id = get_jwt_identity()

    db = SessionLocal()

    recruiter = (
        db.query(Recruiter)
        .filter(Recruiter.id == recruiter_id)
        .first()
    )

    db.close()

    if not recruiter:
        return jsonify({"error": "Recruiter not found"}), 404

    return jsonify({
        "recruiter": recruiter.get_recruiter()
    }), 200