from backend.models.education import Education
from backend.db.session import SessionLocal
from typing import List, Dict

def save_educations_to_db( educations: List[Dict], resume_id: str):
    db = SessionLocal()
    try:
        for edu in educations:
            db.add(Education(
                resume_id=resume_id,
                degree=edu.get("degree"),
                institution=edu.get("institution"),
                cgpa=edu.get("cgpa"),
                start_year=edu.get("start_year"),
                end_year=edu.get("end_year")
            ))
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()