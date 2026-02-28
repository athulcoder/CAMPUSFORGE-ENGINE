import time


from backend.services.candidate_cache import cache_candidate_basic

# Redis queue + status updates
from backend.services.redis_service import (
    dequeue_resume_job,
    update_resume_status
)

# File storage
from backend.services.minio_service import download_from_minio

# Database
from backend.db.session import SessionLocal
from backend.models.resume import Resume, ProcessingStatus

# Resume processing
from backend.resume_worker.parsers.pdf_extractor import parse_pdf
from backend.resume_worker.parsers.resume_parser import parse_resume

# Scoring
from backend.resume_worker.scoring.resume_scoring import score_resume


print("🚀 Resume worker started")

# Worker runs forever
while True:
    try:
        #  Wait for a resume job from Redis (blocking call)
        data = dequeue_resume_job(block=True)

        if not data:
            continue

        resume_id = data["resume_id"]
        bucket = data["bucket"]
        object_name = data["object_name"]

        db = SessionLocal()
        resume = None

        try:
            #  Fetch resume record from DB
            resume = db.get(Resume, resume_id)
            if not resume:
                print(f"⚠️ Resume {resume_id} not found in DB")
                continue

            # STATUS: Parsing started
            update_resume_status(
                resume_id,
                status="PARSING",
                progress=20,
                message="Downloading resume from storage"
            )

            resume.processing_status = ProcessingStatus.PARSING
            db.commit()

            # Download PDF from MinIO
            pdf_bytes = download_from_minio(bucket, object_name)

            update_resume_status(
                resume_id,
                status="PARSING",
                progress=40,
                message="Extracting text from PDF"
            )

            #  Extract raw text from PDF
            raw_text = parse_pdf(pdf_bytes)

            update_resume_status(
                resume_id,
                status="PARSING",
                progress=60,
                message="Extracting structured data"
            )
            
            
            #  Parse resume into structured sections
            parsed_resume = parse_resume(raw_text,resume_id)
            
            
            update_resume_status(
                resume_id,
                status="SCORING",
                progress=80,
                message="Scoring resume & matching job roles"
            )
            
            #  Score resume + match against job roles
            score_data = score_resume(parsed_resume)

            best_match = score_data["best_match"]

            #  Update resume record
            resume.raw_text = raw_text
            resume.resume_score = best_match["score"]
            resume.matched_role = best_match["job_role"]
            resume.processing_status = ProcessingStatus.COMPLETED

            db.commit()

            #  STATUS: Completed
            update_resume_status(
                resume_id,
                status="COMPLETED",
                progress=100,
                message="Resume processed successfully"
            )

            # Get candidate name using relationship
            candidate = resume.candidate
            candidate_name = candidate.full_name if candidate else None

            # Cache minimal candidate data for fast UI access
            cache_candidate_basic({
                "id": resume_id,
                "name": candidate_name,
                "job_role": resume.matched_role,
                "score": resume.resume_score,
                "status": resume.selection_status.value
            })

            print(f"✅ Resume {resume_id} processed successfully")

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

            print(f" Resume {resume_id} failed:", e)

        finally:
            db.close()

    except Exception as outer:
        print("Worker loop error:", outer)
        time.sleep(2)


