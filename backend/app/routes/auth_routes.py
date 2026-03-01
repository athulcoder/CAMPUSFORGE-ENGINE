from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from backend.db.session import SessionLocal
from backend.models.recruiter import Recruiter

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


# REGISTER
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

    recruiter = (
        db.query(Recruiter)
        .filter(Recruiter.email == data["email"])
        .first()
    )

    if not recruiter or not recruiter.check_password(data["password"]):
        db.close()
        return jsonify({"error": "Invalid email or password"}), 401

  
    access_token = create_access_token(identity=recruiter.id)

    db.close()


    return jsonify({
        "message":"Login was successful",
        "success": True,
        "access_token": access_token,     
        "recruiter": recruiter.get_recruiter()
    }), 200



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



@auth_bp.post("/logout")
def logout():
    
    return jsonify({"success": True, "message": "Logged out"}), 200