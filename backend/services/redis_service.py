import os
import json
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True,
)


QUEUE_NAME = "resume_jobs"


def enqueue_resume_job(payload: dict):
    redis_client.lpush(QUEUE_NAME, json.dumps(payload))


def dequeue_resume_job(block: bool = True, timeout: int = 0):
    """
    Blocking pop for workers
    """
    if block:
        _, job = redis_client.brpop(QUEUE_NAME, timeout=timeout)
        return json.loads(job)

    job = redis_client.rpop(QUEUE_NAME)
    return json.loads(job) if job else None