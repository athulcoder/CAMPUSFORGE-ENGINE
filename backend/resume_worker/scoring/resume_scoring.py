from backend.resume_worker.jobs.job_roles import JOB_ROLES
from .skills import score_skills
from .experience import score_experience
from .education import score_education
from .semantic import score_semantic
from backend.resume_worker.extractor.skills.skill_extraction import extract_skills_from_resume


def score_resume(parsed_resume: dict) -> dict:
    """
    Scores resume against all predefined job roles
    and returns the best match
    """
    
    results = []

    for role_name, job in JOB_ROLES.items():
        skill_score = score_skills(
            parsed_resume['skills'],
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

        resume_text = build_resume_semantic(parsed_resume)
        role_text = build_role_semantic(job)

        semantic_score = score_semantic(resume_text, role_text)

        print(f'SKILL SCORE : {skill_score}\n EXP SCORE : {exp_score}\n EDU SCORE : {edu_score}\n SEMATIC SCORE : {semantic_score}\n', flush=True)
        weighted_total = (
            skill_score +
            semantic_score +
            exp_score +
            edu_score
        )

        final_score = round(weighted_total, 2)
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


def build_role_semantic(job: dict) -> dict:
    return {
        "skills": " ".join(
            job.get("skills", {}).get("core", []) +
            job.get("skills", {}).get("secondary", []) +
            job.get("skills", {}).get("bonus", [])
        ).lower(),

        "keywords": " ".join(job.get("role_keywords", [])).lower(),

        "description": job.get("job_description", "").lower()
    }

def build_resume_semantic(parsed_resume: dict) -> dict:
    return {
        "skills": " ".join(parsed_resume.get("skills", [])).lower(),

        "titles": " ".join(
            exp.get("title", "")
            for exp in parsed_resume.get("experience", [])
        ).lower(),

        "content": " ".join(
            exp.get("responsibilities", [])
            for exp in parsed_resume.get("experience", [])
        ).lower()
        + " "
        + " ".join(
            proj.get("description", "")
            for proj in parsed_resume.get("projects", [])
        ).lower()
    }