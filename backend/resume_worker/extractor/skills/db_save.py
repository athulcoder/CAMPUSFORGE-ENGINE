from typing import List, Dict
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from backend.db.session import SessionLocal
from backend.models.skill import Skill
from backend.models.resume_skill import ResumeSkill


def saveSkillsToDB(
    data: List[Dict[str, str]],
    resume_id: str
) -> None:
    """
    Save extracted skills and link them to a resume.

    data = [
        {"skill_name": "python", "category": "language"},
        {"skill_name": "docker", "category": "devops"}
    ]
    """

    if not data:
        return

    db = SessionLocal()
    

    try:
        for item in data:
            skill_name = item["skill_name"]
            category = item.get("category")

            # -------------------------------------------------
            # 1. Get or create Skill
            # -------------------------------------------------
            skill = (
                db.query(Skill)
                .filter(Skill.skill_name == skill_name)
                .first()
            )

            if not skill:
                skill = Skill(
                    skill_name=skill_name,
                    category=category
                )
                db.add(skill)

                try:
                    # flush to get skill.id without committing
                    db.flush()
                except IntegrityError:
                    # another worker inserted same skill
                    db.rollback()
                    skill = (
                        db.query(Skill)
                        .filter(Skill.skill_name == skill_name)
                        .first()
                    )

            # -------------------------------------------------
            # 2. Link Resume <-> Skill (resume_skills table)
            # -------------------------------------------------
            exists = (
                db.query(ResumeSkill)
                .filter(
                    ResumeSkill.resume_id == resume_id,
                    ResumeSkill.skill_id == skill.id
                )
                .first()
            )

            if not exists:
                db.add(
                    ResumeSkill(
                        resume_id=resume_id,
                        skill_id=skill.id,
                        level=None  # you can set later if needed
                    )
                )

        # -------------------------------------------------
        # 3. Commit once (important for performance)
        # -------------------------------------------------
        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()