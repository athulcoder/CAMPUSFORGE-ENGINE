from backend.db.session import SessionLocal
from backend.models.candidate import Candidate


def saveCandidateToDB(data: dict, resume_id:str):
    db = SessionLocal()

    try:
        candidate = Candidate(
            full_name=data.get("full_name"),
            email=data.get("email"),
            phone=data.get("phone"),
            location=data.get("location"),
            resume_id=resume_id
        )

        db.add(candidate)
        db.commit()
        db.refresh(candidate)

        return candidate.id

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()