import re
from typing import List, Dict
from backend.resume_worker.extractor.education.save_db import save_educations_to_db
def extract_education_section(text: str) -> str:
    text_lower = text.lower()

    start_keywords = ["education", "academic background"]
    end_keywords = ["experience", "skills", "projects", "certifications"]

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
            break

    return section.strip()


def extract_cgpa(text: str):
    match = re.search(r"(cgpa|gpa)\s*[:\-]?\s*(\d+(\.\d+)?)", text, re.I)
    if match:
        return float(match.group(2))
    return None

def extract_years(text: str):
    match = re.search(
        r'((?:19|20)\d{2})\s*(?:-|–|to)\s*((?:19|20)\d{2}|present)',
        text.lower()
    )

    if match:
        start = int(match.group(1))
        end = None if match.group(2) == "present" else int(match.group(2))
        return start, end

    single = re.search(r'((?:19|20)\d{2})', text)
    if single:
        return int(single.group(1)), None

    return None, None

def extract_degree_and_institution(lines):
    degree_keywords = [
        "bachelor", "b.tech", "btech", "b.tech", "bachelor of technology",
        "master", "m.tech", "msc", "b.sc", "phd", "mba",
        "12th", "higher secondary", "hss"
    ]

    degree = None
    institution = None

    for line in lines:
        lower = line.lower()

        if not degree and any(k in lower for k in degree_keywords):
            degree = line

        if not institution and any(k in lower for k in ["college", "school", "institute", "university", "hss"]):
            institution = line

    return degree, institution
def parse_educations(section: str):
    educations = []
    if not section:
        return educations

    lines = [l.strip() for l in section.split("\n") if l.strip()]

    current_block = []

    for line in lines:
        current_block.append(line)

        # Split education entry when year range appears
        if re.search(r'(?:19|20)\d{2}\s*(?:-|–)\s*(?:19|20)\d{2}', line):
            block_text = " ".join(current_block)
            block_lines = current_block.copy()

            degree, institution = extract_degree_and_institution(block_lines)
            start_year, end_year = extract_years(block_text)
            cgpa = extract_cgpa(text=section)
            educations.append({
                "degree": degree,
                "institution": institution,
                "cgpa": cgpa,
                "start_year": start_year,
                "end_year": end_year
            })

            current_block = []

    return educations



def format_education_as_text(educations: list) -> str:
    parts = []

    for edu in educations:
        degree = edu.get("degree")
        institution = edu.get("institution")
        start = edu.get("start_year")
        end = edu.get("end_year")
        cgpa = edu.get("cgpa")

        text = []

        if degree:
            text.append(degree)

        if institution:
            text.append(f"at {institution}")

        if start:
            year_part = f"({start}"
            if end:
                year_part += f"–{end}"
            else:
                year_part += "–Present"
            year_part += ")"
            text.append(year_part)

        if cgpa:
            text.append(f"CGPA {cgpa}")

        parts.append(" ".join(text))

    return "; ".join(parts)



def extract_educations_from_resume(text: str, resume_id):
    section = extract_education_section(text)
    educations = parse_educations(section)

    if educations:
        save_educations_to_db(educations, resume_id=resume_id)

    # ✅ return readable string instead of list
    education_text = format_education_as_text(educations)

    return education_text