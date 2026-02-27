import re
from typing import List, Dict
from backend.resume_worker.extractor.education.save_db import save_educations_to_db
def extract_education_section(text: str) -> str:
    if not text:
        return ""

    text_lower = text.lower()

    start_keywords = [
        "education",
        "academic background",
        "educational qualifications"
    ]

    end_keywords = [
        "experience",
        "skills",
        "projects",
        "certifications",
        "achievements"
    ]

    start_idx = -1
    for kw in start_keywords:
        if kw in text_lower:
            start_idx = text_lower.find(kw)
            break

    if start_idx == -1:
        return ""

    section = text[start_idx:]

    for end_kw in end_keywords:
        idx = section.lower().find(end_kw)
        if idx != -1:
            section = section[:idx]

    return section.strip()



def extract_cgpa(text: str):
    match = re.search(r"(cgpa|gpa)\s*[:\-]?\s*(\d+(\.\d+)?)", text, re.I)
    if match:
        return float(match.group(2))
    return None


def extract_years(text: str):
    text = text.lower()

    # Match ranges like: 2019 - 2023, 2019–2023, 2019 to 2023
    range_match = re.search(
        r'((?:19|20)\d{2})\s*(?:-|–|to)\s*((?:19|20)\d{2}|present)',
        text
    )

    if range_match:
        start_year = int(range_match.group(1))
        end_year = (
            None if range_match.group(2) == "present"
            else int(range_match.group(2))
        )
        return start_year, end_year

    # Match single year like: 2021
    single_match = re.search(r'((?:19|20)\d{2})', text)
    if single_match:
        return int(single_match.group(1)), None

    return None, None


def extract_degree_and_institution(lines: List[str]):
    degree_keywords = [
        "bachelor", "master", "b.tech", "btech", "m.tech",
        "b.sc", "m.sc", "phd", "mba", "diploma"
    ]

    degree = None
    institution = None

    for line in lines:
        lower = line.lower()

        if not degree and any(k in lower for k in degree_keywords):
            degree = line

        if not institution and (
            "college" in lower or
            "university" in lower or
            "institute" in lower
        ):
            institution = line

    return degree, institution



def parse_educations(section: str) -> List[Dict]:
    educations = []

    if not section:
        return educations

    # split into blocks (each education)
    blocks = re.split(r"\n\s*\n|•\s+|- ", section)

    for block in blocks:
        block = block.strip()
        if len(block) < 20:
            continue

        lines = [l.strip() for l in block.split("\n") if l.strip()]

        degree, institution = extract_degree_and_institution(lines)
        cgpa = extract_cgpa(block)
        start_year, end_year = extract_years(block)

        educations.append({
            "degree": degree,
            "institution": institution,
            "cgpa": cgpa,
            "start_year": start_year,
            "end_year": end_year
        })

    return educations



def extract_educations_from_resume(text: str,resume_id) -> List[Dict]:
    section = extract_education_section(text)
    save_educations_to_db(parse_educations(section),resume_id=resume_id)