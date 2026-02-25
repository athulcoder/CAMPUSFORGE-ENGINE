from flask import Blueprint, session
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.recruiter import Recruiter

recruiter_bp = Blueprint(
    "recruiter",
    __name__,
    url_prefix="/api/recruiter"
)

@recruiter_bp.get("/me")
@jwt_required()
def get_my_profile():
    recruiter_id = get_jwt_identity()

    recruiter = Recruiter.query.get(recruiter_id)
    if not recruiter:
        return {"error": "Recruiter not found"}, 404

    return {
        "recruiter": recruiter.get_recruiter()
    }, 200