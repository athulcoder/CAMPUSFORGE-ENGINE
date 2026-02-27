import re
from backend.resume_worker.normalization.skills import normalize_skills


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


def parse_resume(text: str) -> dict:
    """
    Parses raw resume text into structured + normalized data.
    Extraction only — no scoring logic here.
    """
    # text = text.lower()
    print(type(text),flush=True)
    skills_section = extract_section(text, "technical skills", "projects")
    education_section = extract_section(text, "education", "technical skills")
    experience_section = extract_section(text, "experience", "education")

    raw_skills = extract_skills(skills_section)
    normalized_skills = normalize_skills(raw_skills)

    education_level = extract_highest_education_level(education_section)
    total_experience_years = extract_years_of_experience(experience_section)

    return {
        "skills": normalized_skills,                 # ✅ normalized once
        "education_level": education_level,           # 0–4
        "total_experience_years": total_experience_years,
        "education_text": education_section,
        "experience_text": experience_section,
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
    """
    Extract maximum years of experience mentioned.
    Examples matched:
    - "3 years"
    - "5+ years"
    - "2 yrs"
    """
    if not text:
        return 0.0

    matches = re.findall(r"(\d+)\+?\s*(years|year|yrs|yr)", text)
    years = [int(m[0]) for m in matches]

    return float(max(years)) if years else 0.0