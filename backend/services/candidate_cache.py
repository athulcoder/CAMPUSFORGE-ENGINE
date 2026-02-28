import redis
import json
from backend.models.resume import Resume, ProcessingStatus
from .candidate_service import fetch_candidates_from_db
from backend.db.session import SessionLocal

r = redis.Redis(host="redis", port=6379, decode_responses=True)


def cache_candidate_basic(candidate):
    """
    candidate = {
        id,
        name,
        job_role,
        score,
        status
    }
    """
    cid = candidate["id"]
    score = candidate["score"]
    role = candidate["job_role"]
    status = candidate["status"]

    # Store candidate basic data
    r.set(
        f"candidate:basic:{cid}",
        json.dumps(candidate)
    )

    # Global score index
    r.zadd("candidates:by_score", {cid: score})

    # Role-based score index
    r.zadd(f"candidates:role:{role}", {cid: score})

    # Status-based score index
    r.zadd(f"candidates:status:{status}", {cid: score})

    # Role + Status score index
    r.zadd(
        f"candidates:role:{role}:status:{status}",
        {cid: score}
    )


def get_candidates_by_role(role="All", status="PENDING", limit=50):
    """
    Fetch candidates using Redis-first strategy with role and status filtering.
    Falls back to DB if Redis miss occurs.
    """

    # Decide Redis key (NO ALL STATUS)
    if role == "All":
        redis_key = f"candidates:status:{status}"
    else:
        redis_key = f"candidates:role:{role}:status:{status}"

    # Attempt Redis fetch
    ids = (
        r.zrevrange(redis_key, 0, limit - 1)
        if r.exists(redis_key)
        else []
    )

    candidates = [
        json.loads(r.get(f"candidate:basic:{cid}"))
        for cid in ids
        if r.exists(f"candidate:basic:{cid}")
    ]

    # Redis hit only if fully populated
    if candidates and len(candidates) == len(ids):
        return candidates

    # Redis miss → DB fallback
    db_candidates = fetch_candidates_from_db(role, status, limit)
    print(db_candidates, "FROM ATHUL")
    # Repopulate Redis
    for c in db_candidates:
        cache_candidate_basic(c)

    return db_candidates

def get_candidate_basic(candidate_id):
    """
    Fetch single candidate basic data from Redis or DB.
    """

    data = r.get(f"candidate:basic:{candidate_id}")
    if data:
        return json.loads(data)

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
            "status": rsm.selection_status.value,
        }

        cache_candidate_basic(candidate)
        return candidate

    finally:
        db.close()


def update_candidate_status(candidate_id, old_status, new_status, role, score):
    """
    Update Redis indexes when a candidate is approved or rejected.
    Must be called after DB commit.
    """

    # Remove old status indexes
    r.zrem(f"candidates:status:{old_status}", candidate_id)
    r.zrem(f"candidates:role:{role}:status:{old_status}", candidate_id)

    # Add new status indexes
    r.zadd(f"candidates:status:{new_status}", {candidate_id: score})
    r.zadd(
        f"candidates:role:{role}:status:{new_status}",
        {candidate_id: score}
    )

    # Update cached object
    data = r.get(f"candidate:basic:{candidate_id}")
    if data:
        obj = json.loads(data)
        obj["status"] = new_status
        r.set(f"candidate:basic:{candidate_id}", json.dumps(obj))