import redis
import json
import os

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True,
)

def enqueue_resume_job(payload: dict):
    redis_client.lpush("resume_jobs", json.dumps(payload))