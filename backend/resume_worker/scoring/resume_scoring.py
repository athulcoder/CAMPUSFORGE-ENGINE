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

    for role_name, job in JOB_ROLES.items():
        skill_score = score_skills(
            parsed_resume["skills"],
            job["skills"]
        )

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

        weighted_total = (
            0.4 * skill_score +
            0.2 * semantic_score +
            0.3 * exp_score +
            0.1 * edu_score
        )

        final_score = round(weighted_total * 100, 2)
        print(final_score,flush=True)

        
        results.append({
            "job_role": role_name,   
            "score": float(min(final_score, 100)),
            "breakdown": {
                "skills": round(skill_score, 2),
                "experience": round(exp_score, 2),
                "education": round(edu_score, 2),
                "semantic": round(semantic_score, 2),
            }
        })

    # Best match first
    results.sort(key=lambda x: x["score"], reverse=True)

    return {
        "best_match": results[0],
        "all_matches": results
    }