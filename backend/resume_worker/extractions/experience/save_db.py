from backend.models.experience import Experience
from backend.db.session import SessionLocal
def save_experiences_to_db( experiences: list[dict],resume_id: str):
    db = SessionLocal()
    try:
        for exp in experiences:
            experience = Experience(
                resume_id=resume_id,
                job_title=exp.get("job_title"),
                company=exp.get("company"),
                description=exp.get("description"),
                start_date=exp.get("start_date"),
                end_date=exp.get("end_date"),
            )
            db.add(experience)

        db.commit()

    except Exception:
        db.rollback()
        raise
    finally:
        db.close()