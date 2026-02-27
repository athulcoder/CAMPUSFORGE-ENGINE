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



def update_resume_status(resume_id: str, status: str, progress: int = None, message: str = None):
    payload = {
        "resume_id": resume_id,
        "status": status,
        "progress": progress,
        "message": message
    }

    # Store latest state
    redis_client.set(
        f"resume:status:{resume_id}",
        json.dumps(payload),
        ex=3600
    )

    # Publish event
    redis_client.publish(
        f"resume:channel:{resume_id}",
        json.dumps(payload)
    )