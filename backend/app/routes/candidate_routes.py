from flask import Blueprint, request, jsonify
from backend.services.candidate_cache import (
    get_candidates_by_role,
    cache_candidate_basic
)

from backend.services.candidate_service import get_candidate_full
candidate_bp = Blueprint("candidate", __name__ ,url_prefix="/api" )


# 🔹 FAST LIST API (REDIS ONLY)
@candidate_bp.route("/candidate", methods=["GET"])
def list_candidates():
    role = request.args.get("role", "All")
    status = request.args.get("status")
    candidates = get_candidates_by_role(role,status)

    return jsonify({
        "candidates": candidates
    })


@candidate_bp.route("/candidate/<resume_id>", methods=["GET"])
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


