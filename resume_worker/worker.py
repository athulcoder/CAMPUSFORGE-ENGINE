from redis_client import redis_client
from db import SessionLocal
from models import Resume
from parser import parse_resume

import json
import time
print("🚀 PDF resume worker started", flush=True)

QUEUE_NAME = "resume_jobs"

while True:
    try:
        job = redis_client.brpop(QUEUE_NAME, timeout=5)
        if not job:
            continue

        _, payload = job
        data = json.loads(payload)

        db = SessionLocal()
        resume = db.get(Resume, data["resume_id"])

        if not resume:
            print("❌ Resume not found:", data["resume_id"], flush=True)
            db.close()
            continue

        resume.processing_status = "PARSING"
        db.commit()

        raw_text, score = parse_resume(data)

        resume.processing_status = "CALCULATING_SCORE"
        resume.raw_text = raw_text
        resume.resume_score = score
        db.commit()

        resume.processing_status = "COMPLETED"
        db.commit()

        db.close()

        print(f"✅ Resume {resume.id} parsed", flush=True)

    except Exception as e:
        print("🔥 Worker error:", e, flush=True)
        time.sleep(2)