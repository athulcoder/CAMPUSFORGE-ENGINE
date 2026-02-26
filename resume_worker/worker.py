from backend.services.redis_service import redis_client
from backend.db.session import SessionLocal
from backend.models.resume import Resume, ProcessingStatus
from parser.pdf_parser import parse_pdf_text
from backend.services.minio_service import download_from_minio
import json
import time

print("🚀 Resume worker started")

while True:
    try:
        _, job = redis_client.brpop("resume_jobs")
        data = json.loads(job)

        db = SessionLocal()

        resume = db.query(Resume).get(data["resume_id"])
        if not resume:
            db.close()
            continue

        resume.processing_status = ProcessingStatus.PARSING
        db.commit()

        pdf_bytes = download_from_minio(
            data["bucket"],
            data["object_name"]
        )

        raw_text, score = parse_pdf_text(pdf_bytes)

        resume.raw_text = raw_text
        resume.resume_score = score
        resume.processing_status = ProcessingStatus.COMPLETED

        db.commit()
        db.close()

        print(f"✅ Resume {resume.id} parsed")

    except Exception as e:
        print("🔥 Worker error:", e)
        time.sleep(2)