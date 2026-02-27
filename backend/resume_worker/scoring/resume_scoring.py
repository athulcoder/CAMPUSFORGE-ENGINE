from backend.resume_worker.jobs.job_roles import JOB_ROLES
from .skills import score_skills
from .experience import score_experience
from .education import score_education
from .semantic import score_semantic


def score_resume(parsed_resume: dict) -> dict:
    """
    Scores resume against all predefined job roles
    and returns the best match
    """

    results = []

    for job in JOB_ROLES:
        skill_score = score_skills(
            parsed_resume["skills"],
            job["skills"]
        )
        print("Working here athuleee",flush=True)
        exp_score = score_experience(
            parsed_resume["total_experience_years"],
            job["min_experience_years"]
        )

        edu_score = score_education(
            parsed_resume.get("education_level"),
            job["education_keywords"]
        )

        semantic_score = score_semantic(
            parsed_resume["raw_text"],
            job["job_description"]
        )

        total = round(
            skill_score + exp_score + edu_score + semantic_score,
            2
        )

        results.append({
            "job_role": job["role"],
            "score": min(total, 100),
            "breakdown": {
                "skills": round(skill_score, 2),
                "experience": round(exp_score, 2),
                "education": round(edu_score, 2),
                "semantic": round(semantic_score, 2),
            }
        })

    # 🔥 Best match first
    results.sort(key=lambda x: x["score"], reverse=True)

    return {
        "best_match": results[0],
        "all_matches": results
    }