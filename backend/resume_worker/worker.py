import time

from backend.services.redis_service import dequeue_resume_job
from backend.services.minio_service import download_from_minio
from backend.db.session import SessionLocal
from backend.models.resume import Resume, ProcessingStatus

from backend.resume_worker.parsers.pdf_extractor import extract_text_from_pdf as parse_pdf
from backend.resume_worker.scoring.resume_scoring import score_resume

print("🚀 Resume worker started")

while True:
    try:
        # 1️⃣ Wait for a job (blocking)
        data = dequeue_resume_job(block=True)

        if not data:
            continue

        resume_id = data["resume_id"]
        bucket = data["bucket"]
        object_name = data["object_name"]

        db = SessionLocal()
        resume = None

        try:
            # 2️⃣ Fetch resume row
            resume = db.get(Resume, resume_id)
            if not resume:
                print(f"⚠️ Resume {resume_id} not found")
                continue

            # 3️⃣ Mark PARSING
            resume.processing_status = ProcessingStatus.PARSING
            db.commit()

            # 4️⃣ Download PDF from MinIO
            pdf_bytes = download_from_minio(bucket, object_name)

            # 5️⃣ Parse PDF
            raw_text = parse_pdf(pdf_bytes)

            # 6️⃣ Score resume
            score = score_resume(raw_text)

            # 7️⃣ Save results
            resume.raw_text = raw_text
            resume.resume_score = score
            resume.processing_status = ProcessingStatus.COMPLETED

            db.commit()
            print(f"✅ Resume {resume_id} parsed successfully")

        except Exception as e:
            db.rollback()
            if resume:
                resume.processing_status = ProcessingStatus.FAILED
                db.commit()
            print(f"🔥 Resume {resume_id} failed:", e)

        finally:
            db.close()

    except Exception as outer:
        print("🔥 Worker loop error:", outer)
        time.sleep(2)