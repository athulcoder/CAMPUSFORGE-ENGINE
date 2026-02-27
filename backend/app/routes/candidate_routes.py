from flask import Blueprint, request, jsonify
from backend.services.candidate_cache import (
    get_candidates_by_role,
    get_candidate_basic
)
from backend.app.routes.candidate_repo import get_candidate_full

candidate_bp = Blueprint("candidate", __name__ ,url_prefix="/api" )


# 🔹 FAST LIST API (REDIS ONLY)
@candidate_bp.route("/candidate", methods=["GET"])
def list_candidates():
    role = request.args.get("role", "All")

    candidates = get_candidates_by_role(role)

    return jsonify({
        "candidates": candidates
    })


# 🔹 FULL PROFILE API (DB HIT)
@candidate_bp.route("/candidate/<candidate_id>", methods=["GET"])
def get_candidate(candidate_id):
    # optional: show basic info instantly
    basic = get_candidate_basic(candidate_id)

    full = get_candidate_full(candidate_id)
    if not full:
        return jsonify({"error": "Candidate not found"}), 404

    # merge redis + db data
    if basic:
        full.update(basic)

    return jsonify(full)