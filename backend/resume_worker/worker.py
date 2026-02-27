import time

from backend.services.redis_service import dequeue_resume_job,update_resume_status
from backend.services.minio_service import download_from_minio
from backend.db.session import SessionLocal
from backend.models.resume import Resume, ProcessingStatus
from backend.resume_worker.extractions.extract_all import extract_all_and_save_to_db
from backend.resume_worker.parsers.pdf_extractor import  parse_pdf
from backend.resume_worker.scoring.resume_scoring import score_resume

print("🚀 Resume worker started")

while True:
    try:
        data = dequeue_resume_job(block=True)
        if not data:
            continue

        resume_id = data["resume_id"]
        bucket = data["bucket"]
        object_name = data["object_name"]

        db = SessionLocal()
        resume = None

        try:
            resume = db.get(Resume, resume_id)
            if not resume:
                continue

            # 🔔 STATUS: parsing started
            update_resume_status(
                resume_id,
                status="PARSING",
                progress=20,
                message="Downloading resume"
            )

            resume.processing_status = ProcessingStatus.PARSING
            db.commit()

            pdf_bytes = download_from_minio(bucket, object_name)

            update_resume_status(
                resume_id,
                status="PARSING",
                progress=40,
                message="Extracting text"
            )

            raw_text = parse_pdf(pdf_bytes)

            update_resume_status(
                resume_id,
                status="PARSING",
                progress=60,
                message="Extracting structured data"
            )

            extract_all_and_save_to_db(raw_text, resume_id)

            update_resume_status(
                resume_id,
                status="SCORING",
                progress=80,
                message="Scoring resume"
            )

            score_data = score_resume(raw_text)

            resume.raw_text = raw_text
            resume.resume_score = score_data["score"]
            resume.matched_role = score_data.get("matched_role")
            resume.processing_status = ProcessingStatus.COMPLETED

            db.commit()

            update_resume_status(
                resume_id,
                status="COMPLETED",
                progress=100,
                message="Resume processed successfully"
            )

            print(f"✅ Resume {resume_id} completed")

        except Exception as e:
            db.rollback()
            if resume:
                resume.processing_status = ProcessingStatus.FAILED
                db.commit()

            update_resume_status(
                resume_id,
                status="FAILED",
                progress=0,
                message=str(e)
            )

            print(f"🔥 Resume {resume_id} failed:", e)

        finally:
            db.close()

    except Exception as outer:
        print("🔥 Worker loop error:", outer)
        time.sleep(2)