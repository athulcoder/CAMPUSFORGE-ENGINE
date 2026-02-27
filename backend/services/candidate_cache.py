import redis
import json

r = redis.Redis(host="redis", port=6379, decode_responses=True)

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
    if role == "All":
        ids = r.zrevrange("candidates:by_score", 0, limit - 1)
    else:
        ids = r.zrevrange(f"candidates:role:{role}", 0, limit - 1)

    return [
        json.loads(r.get(f"candidate:basic:{cid}"))
        for cid in ids
        if r.exists(f"candidate:basic:{cid}")
    ]

def get_candidate_basic(candidate_id):
    data = r.get(f"candidate:basic:{candidate_id}")
    return json.loads(data) if data else None   