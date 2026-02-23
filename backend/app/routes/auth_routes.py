from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.models.recruiter import Recruiter
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.post("/register")
def register():
    data = request.get_json()

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password required"}), 400

    recruiter = Recruiter(
        email=data["email"],
        name=data.get("name", "")
    )
    recruiter.set_password(data["password"])

    try:
        db.session.add(recruiter)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists"}), 400


    return jsonify({
        "message": "Recruiter registered successfully",
        "id": recruiter.id
    }), 201


@auth_bp.post("/login")
def login():
    data = request.get_json()

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password required"}), 400

    recruiter = Recruiter.query.filter_by(email=data["email"]).first()

    if not recruiter or not recruiter.check_password(data["password"]):
        return jsonify({"error": "Invalid email or password"}), 401


    access_token = create_access_token(identity=recruiter.id)
    return jsonify({
        "message": "Login successful",
        "access_token":access_token,
        "recruiter": recruiter.get_recruiter()
    }), 200


@auth_bp.get("/me")
@jwt_required()
def me():
    recruiter_id = get_jwt_identity()

    recruiter = Recruiter.query.get(recruiter_id)
    if not recruiter:
        return {"error": "User not found"}, 404

    return {
        "recruiter": recruiter.to_dict()
    }, 200



