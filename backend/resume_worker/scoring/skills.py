from backend.resume_worker.normalization.skills import normalize_skills

JOB_SKILLS = {
    "backend_developer": {
        "python", "nodejs", "postgresql", "rest", "docker"
    }
}

def score_skills(text: str, job_role: str) -> float:
    resume_skills = normalize_skills(text)
    required = JOB_SKILLS.get(job_role, set())

    if not required:
        return 0.0

    matched = resume_skills & required
    return (len(matched) / len(required)) * 40