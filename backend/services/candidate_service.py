from backend.db.session import SessionLocal
from backend.models.candidate import Candidate
from backend.models.resume import Resume
from backend.models.skill import Skill
from backend.models.resume_skill import ResumeSkill
from backend.models.experience import Experience
from backend.models.education import Education
from backend.models.project import Project


def get_candidate_full(resume_id: str) -> dict:
    db = SessionLocal()

    try:
        # -------------------------------------------------
        # 1️⃣ Resume (PRIMARY ENTRY POINT)
        # -------------------------------------------------
        resume = db.query(Resume).filter_by(id=resume_id).first()
        if not resume:
            return {}

        # -------------------------------------------------
        # 2️⃣ Candidate (via resume)
        # -------------------------------------------------
        candidate = (
            db.query(Candidate)
            .filter_by(resume_id=resume.id)
            .first()
        )

        # -------------------------------------------------
        # 3️⃣ Skills
        # -------------------------------------------------
        skills = (
            db.query(Skill.skill_name)
            .join(ResumeSkill, Skill.id == ResumeSkill.skill_id)
            .filter(ResumeSkill.resume_id == resume.id)
            .all()
        )

        # -------------------------------------------------
        # 4️⃣ Experience
        # -------------------------------------------------
        experiences = (
            db.query(Experience)
            .filter_by(resume_id=resume.id)
            .order_by(Experience.start_date.desc())
            .all()
        )

        # -------------------------------------------------
        # 5️⃣ Education
        # -------------------------------------------------
        educations = (
            db.query(Education)
            .filter_by(resume_id=resume.id)
            .order_by(Education.end_year.desc())
            .all()
        )

        # -------------------------------------------------
        # 6️⃣ Projects
        # -------------------------------------------------
        projects = (
            db.query(Project)
            .filter_by(resume_id=resume.id)
            .all()
        )

        # -------------------------------------------------
        # 7️⃣ Response (Frontend-ready)
        # -------------------------------------------------
        return {
            "id": resume.id,  # IMPORTANT: resume id (not candidate id)
            "name": candidate.full_name if candidate else "",
            "role": resume.maching_role,
            "score": resume.resume_score,

            "skills": [s[0] for s in skills],

            "experience": [
                {
                    "company": e.company,
                    "role": e.job_title,
                    "duration": f"{e.start_date} – {e.end_date or 'Present'}",
                    "description": e.description,
                }
                for e in experiences
            ],

            "education": [
                {
                    "institute": edu.institution,
                    "degree": edu.degree,
                    "year": f"{edu.start_year} – {edu.end_year}",
                }
                for edu in educations
            ],

            "projects": [
                {
                    "name": p.project_title,
                    "description": p.description,
                    "githubRepo":p.github_repo,
                    "tech stack":p.tech_stack,
                }
                for p in projects
            ],
        }

    finally:
        db.close()




from sqlalchemy import desc
from backend.db.session import SessionLocal
from backend.models.resume import Resume, ProcessingStatus

def fetch_candidates_from_db(role=None, limit=50):
    db = SessionLocal()
    try:
        q = (
            db.query(Resume)
            .filter(Resume.processing_status == ProcessingStatus.COMPLETED)
        )

        if role and role != "All":
            q = q.filter(Resume.maching_role == role)

        resumes = (
            q.order_by(desc(Resume.resume_score))
             .limit(limit)
             .all()
        )

        return [
            {
                "id": r.id,
                "name": r.candidate.full_name if r.candidate else None,
                "job_role": r.maching_role,
                "score": r.resume_score,
            }
            for r in resumes
        ]
    finally:
        db.close()