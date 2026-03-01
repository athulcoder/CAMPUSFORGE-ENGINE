from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
   

from backend.services.candidate_cache import (
    get_candidates_by_role,
    cache_candidate_basic
)

from backend.services.candidate_service import get_candidate_full
candidate_bp = Blueprint("candidate", __name__ ,url_prefix="/api" )


@candidate_bp.route("/candidate", methods=["GET"])
@jwt_required()
def list_candidates():
    role = request.args.get("role", "All")
    status = request.args.get("status")
    candidates = get_candidates_by_role(role,status)

    return jsonify({
        "candidates": candidates
    })


@candidate_bp.route("/candidate/<resume_id>", methods=["GET"])
@jwt_required()
def get_candidate(resume_id: str):
    """
    Full candidate profile API
    Uses resume_id (not candidate_id)
    Combines Redis + DB data
    """

    full = get_candidate_full(resume_id)

    if not full:
        return jsonify({"error": "Candidate not found"}), 404

   

    return jsonify(full), 200


