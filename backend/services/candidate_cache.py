import redis
import json

r = redis.Redis(host="redis", port=6379, decode_responses=True)


def cache_candidate_basic(candidate):
    """
    candidate = {id, name, role, score}
    """
    cid = candidate["id"]

    # store basic info
    r.set(
        f"candidate:basic:{cid}",
        json.dumps(candidate)
    )

    # index by role
    r.sadd(f"candidate:role:{candidate['job_role']}", cid)


def get_candidates_by_role(role):
    if role == "All":
        keys = r.keys("candidate:basic:*")
        return [
            json.loads(r.get(k))
            for k in keys
            if r.get(k)
        ]

    ids = r.smembers(f"candidate:role:{role}")
    return [
        json.loads(r.get(f"candidate:basic:{cid}"))
        for cid in ids
        if r.exists(f"candidate:basic:{cid}")
    ]


def get_candidate_basic(candidate_id):
    data = r.get(f"candidate:basic:{candidate_id}")
    return json.loads(data) if data else None