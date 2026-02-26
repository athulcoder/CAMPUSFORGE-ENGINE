from flask import Blueprint, request, jsonify, make_response
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from backend.db.session import SessionLocal
from backend.models.recruiter import Recruiter

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.post("/register")
def register():
    data = request.get_json()

    if not data or not data.get("email") or not data.get("password") or not data.get("name"):
        return jsonify({"error": "All fields are required"}), 400

    db = SessionLocal()

    recruiter = Recruiter(
        email=data["email"],
        name=data["name"]
    )
    recruiter.set_password(data["password"])

    try:
        db.add(recruiter)
        db.commit()
    except IntegrityError:
        db.rollback()
        return jsonify({"error": "Email already exists"}), 400
    finally:
        db.close()

    return jsonify({
        "success": True,
        "message": "Recruiter registered successfully"
    }), 201


@auth_bp.post("/login")
def login():
    data = request.get_json()

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password required"}), 400

    db = SessionLocal()

    recruiter = db.query(Recruiter)\
        .filter(Recruiter.email == data["email"])\
        .first()

    if not recruiter or not recruiter.check_password(data["password"]):
        db.close()
        return jsonify({"success": False, "error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=recruiter.id)

    response = make_response(jsonify({
        "success": True,
        "message": "Login successful",
        "recruiter": recruiter.get_recruiter()
    }))

    response.set_cookie(
        "sessionId",
        access_token,
        httponly=True,
        secure=True,       # must be True in prod
        samesite="None",
        max_age=60 * 60 * 24 * 7
    )

    db.close()
    return response, 200


@auth_bp.get("/me")
@jwt_required()
def me():
    recruiter_id = get_jwt_identity()

    db = SessionLocal()
    recruiter = db.query(Recruiter).filter(Recruiter.id == recruiter_id).first()
    db.close()

    if not recruiter:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "recruiter": recruiter.get_recruiter()
    }), 200