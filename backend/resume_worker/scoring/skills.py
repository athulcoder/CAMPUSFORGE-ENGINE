from typing import List, Dict, Set

MAX_SKILL_SCORE = 40.0

WEIGHTS = {
    "core": 0.7,       # must-have skills
    "secondary": 0.2,  # good-to-have
    "bonus": 0.1       # nice extras
}


def score_skills(
    resume_skills: List[str],
    job_skills: Dict[str, List[str]]
) -> float:
    

    print(f"RESUME SKILLS {resume_skills}\n JOB_SKILLS ")
    """
    Score resume skills against ONE job role.

    resume_skills : normalized skill list from parser
    job_skills    : role skill definition (core / secondary / bonus)

    Returns skill score in range 0–40
    """

    if not resume_skills or not job_skills:
        return 0.0

    resume_skill_set: Set[str] = set(resume_skills)
    score = 0.0

    for category, required_skills in job_skills.items():
        if not required_skills:
            continue

        required_skill_set = set(required_skills)
        matched_skills = resume_skill_set & required_skill_set
        

        ratio = len(matched_skills) / len(required_skill_set)
        weight = WEIGHTS.get(category, 0)

        score += ratio * weight * MAX_SKILL_SCORE

    return round(score, 2)


