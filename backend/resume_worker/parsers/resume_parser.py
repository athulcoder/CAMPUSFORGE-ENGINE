import re

def parse_resume(text: str) -> dict:
    text = text.lower()

    skills_section = extract_section(text, "technical skills", "projects")
    education_section = extract_section(text, "education", "technical skills")
    experience_section = extract_section(text, "projects", "education")

    return {
        "skills": extract_skills(skills_section),
        "education": education_section,
        "experience_text": experience_section,
        "raw_text": text
    }

def extract_section(text, start, end):
    try:
        return text.split(start)[1].split(end)[0]
    except IndexError:
        return ""

def extract_skills(text):
    return re.split(r",|\n|•|-", text)