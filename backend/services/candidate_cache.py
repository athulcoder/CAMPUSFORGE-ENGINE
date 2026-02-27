import redis
import json
from backend.models.resume import Resume,ProcessingStatus
from .candidate_service import fetch_candidates_from_db
r = redis.Redis(host="redis", port=6379, decode_responses=True)
from backend.db.session import SessionLocal
def cache_candidate_basic(candidate):
    """
    candidate = {id, name, job_role, score}
    """
    cid = candidate["id"]
    score = candidate["score"]
    role = candidate["job_role"]

    # store basic info
    r.set(
        f"candidate:basic:{cid}",
        json.dumps(candidate)
    )

    # 🔥 GLOBAL sorted index
    r.zadd(
        "candidates:by_score",
        {cid: score}
    )

    # 🔥 ROLE-based sorted index
    r.zadd(
        f"candidates:role:{role}",
        {cid: score}
    )
def get_candidates_by_role(role, limit=50):
    # 1️⃣ Try Redis
    if role == "All":
        ids = r.zrevrange("candidates:by_score", 0, limit - 1)
    else:
        ids = r.zrevrange(f"candidates:role:{role}", 0, limit - 1)

    candidates = [
        json.loads(r.get(f"candidate:basic:{cid}"))
        for cid in ids
        if r.exists(f"candidate:basic:{cid}")
    ]

    # ✅ Redis hit
    if candidates:
        return candidates

    # 2️⃣ Redis miss → DB fallback
    db_candidates = fetch_candidates_from_db(role, limit)

    # 3️⃣ Repopulate Redis
    for c in db_candidates:
        cache_candidate_basic(c)

    return db_candidates
def get_candidate_basic(candidate_id):
    data = r.get(f"candidate:basic:{candidate_id}")
    if data:
        return json.loads(data)

    # Redis miss → DB
    db = SessionLocal()
    try:
        rsm = db.get(Resume, candidate_id)
        if not rsm or rsm.processing_status != ProcessingStatus.COMPLETED:
            return None

        candidate = {
            "id": rsm.id,
            "name": rsm.candidate.full_name if rsm.candidate else None,
            "job_role": rsm.matched_role,
            "score": rsm.resume_score,
        }

        # repopulate Redis
        cache_candidate_basic(candidate)

        return candidate
    finally:
        db.close()