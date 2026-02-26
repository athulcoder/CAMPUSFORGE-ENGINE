from .skills import score_skills
from .experience import score_experience
from .education import score_education
from .semantic import score_semantic

def score_resume(text: str, job_role: str = "backend_developer") -> dict:
    skill_score = score_skills(text, job_role)
    exp_score = score_experience(text)
    edu_score = score_education(text)
    semantic_score = score_semantic(text, job_role)

    total = round(
        skill_score + exp_score + edu_score + semantic_score,
        2
    )

    return {
        "score": min(total, 100),
        "breakdown": {
            "skills": round(skill_score, 2),
            "experience": round(exp_score, 2),
            "education": round(edu_score, 2),
            "semantic": round(semantic_score, 2),
        },
        "job_role": job_role
    }