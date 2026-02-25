import redis
import json
import os
import redis

redis_client = redis.Redis(
    host="redis",  
    port=6379,
    decode_responses=True
)
def enqueue_resume_job(payload: dict):
    redis_client.lpush("resume_jobs", json.dumps(payload))