from backend.resume_worker.jobs.job_roles import JOB_ROLES
from backend.resume_worker.jobs.job_matching import (
    score_skills,
    score_experience,
    score_semantic,
    score_education
)

def match_resume_to_jobs(parsed_resume):
    results = []

    for job in JOB_ROLES:
        skill_score = score_skills(
            parsed_resume["skills"],
            job["skills"]
        )

        exp_score = score_experience(
            parsed_resume["total_experience_years"],
            job["min_experience"]
        )

        semantic_score = score_semantic(
            parsed_resume["raw_text"],
            job["description"]
        )

        edu_score = score_education(
            parsed_resume["degree"],
            job["education"]
        )

        total_score = (
            skill_score +
            exp_score +
            semantic_score +
            edu_score
        )

        results.append({
            "role": job["role"],
            "score": round(total_score, 2),
            "breakdown": {
                "skills": round(skill_score, 2),
                "experience": round(exp_score, 2),
                "semantic": round(semantic_score, 2),
                "education": round(edu_score, 2),
            }
        })

    # Sort best match first
    results.sort(key=lambda x: x["score"], reverse=True)

    return results