import re
from backend.resume_worker.normalization.skills import normalize_skills
from backend.resume_worker.extractor.skills.skill_extraction import extract_skills_from_resume
from backend.resume_worker.extractor.education.education_extraction import extract_educations_from_resume
from backend.resume_worker.extractor.candidate.candidate_extraction import extract_candidate
from backend.resume_worker.extractor.experience.experience_extraction import extract_experiences_from_resume

# ---------------------------------------------------------
# Education keyword hierarchy (highest wins)
# ---------------------------------------------------------
EDUCATION_KEYWORDS = {
    4: [
        "phd", "doctorate", "doctor of philosophy"
    ],
    3: [
        "master", "m.tech", "mtech", "m.sc", "msc",
        "m.s", "ms", "mba"
    ],
    2: [
        "bachelor", "b.tech", "btech", "b.e", "be",
        "b.sc", "bsc", "b.s", "bs"
    ],
    1: [
        "diploma", "polytechnic", "certificate"
    ]
}


def parse_resume(text: str,resume_id:str) -> dict:
    """
    Parses raw resume text into structured + normalized data.
    Extraction only — no scoring logic here.
    """
    text = text.lower()

    # EXTRACTING CANDIDATE 
    extract_candidate(text,resume_id)
    #EXTRACTING EDUCATION STRING 
    education_string = extract_educations_from_resume(text,resume_id)
    #EXTRACTING THE SKILLS AS ARRAY
    myskills =    extract_skills_from_resume(text,resume_id)

    #EXTRACTING EXPERIENCES  
    experience_text = extract_experiences_from_resume(text,resume_id)

    
    education_level = extract_highest_education_level(education_string)
    total_experience_years = extract_years_of_experience(experience_text)
    
    return {
        "skills": myskills,   # normalized skills
        "education_level": education_level,           
        "total_experience_years": total_experience_years,
        "education_text": education_string,
        "experience_text": experience_text,
        "raw_text": text
    }


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

def extract_section(text: str, start: str, end: str) -> str:
    try:
        return text.split(start, 1)[1].split(end, 1)[0]
    except IndexError:
        return ""


def extract_skills(text: str) -> list[str]:
    """
    Extract raw skill tokens from skills section
    """
    if not text:
        return []

    skills = re.split(r",|\n|•|-", text)
    return [s.strip() for s in skills if s.strip()]


def extract_highest_education_level(text: str) -> int:
    """
    Detect highest education level (0–4)
    """
    if not text:
        return 0

    for level in sorted(EDUCATION_KEYWORDS.keys(), reverse=True):
        for keyword in EDUCATION_KEYWORDS[level]:
            if re.search(rf"\b{re.escape(keyword)}\b", text):
                return level

    return 0


def extract_years_of_experience(text: str) -> float:
    # """
    # Extract maximum years of experience mentioned.
    # Examples matched:
    # - "3 years"
    # - "5+ years"
    # - "2 yrs"
    # """
    if not text:
        return 0.0

    matches = re.findall(r"(\d+)\+?\s*(years|year|yrs|yr)", text)
    years = [int(m[0]) for m in matches]

    return float(max(years)) if years else 0.0