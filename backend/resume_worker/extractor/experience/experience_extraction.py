import re
from datetime import date
from typing import List, Dict, Optional
from  backend.resume_worker.extractor.experience.save_db import save_experiences_to_db
def extract_experience_section(text: str) -> str:
    """
    Extracts the experience section from resume text.
    """
    if not text:
        return ""

    text_lower = text.lower()

    start_keywords = [
        "experience",
        "work experience",
        "professional experience",
        "employment history"
    ]

    end_keywords = [
        "education",
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


def extract_dates(text: str) -> tuple[Optional[date], Optional[date]]:
    """
    Extracts start and end dates from text.
    Supports:
    - 2021 - 2023
    - Jan 2021 – Mar 2023
    - 2022 - Present
    """
    year_range = re.search(
        r"(20\d{2}).{0,10}(20\d{2}|present)",
        text,
        re.IGNORECASE
    )

    if not year_range:
        return None, None

    start_year = int(year_range.group(1))
    end_raw = year_range.group(2).lower()

    start_date = date(start_year, 1, 1)

    if end_raw == "present":
        end_date = None
    else:
        end_date = date(int(end_raw), 1, 1)

    return start_date, end_date



def extract_title_company(line: str) -> tuple[Optional[str], Optional[str]]:
    """
    Attempts to extract job title and company from a single line.
    """
    separators = [" at ", " - ", " – ", "|", "@"]

    for sep in separators:
        if sep in line:
            parts = line.split(sep, 1)
            return parts[0].strip(), parts[1].strip()

    return None, None



def parse_experiences(section: str) -> List[Dict]:
    """
    Parses multiple experiences from the experience section.
    """
    experiences = []

    if not section:
        return experiences

    # Split on blank lines or bullet boundaries
    blocks = re.split(r"\n\s*\n|•\s+|- ", section)

    for block in blocks:
        block = block.strip()
        if len(block) < 30:
            continue

        lines = [l.strip() for l in block.split("\n") if l.strip()]
        if not lines:
            continue

        job_title, company = extract_title_company(lines[0])
        start_date, end_date = extract_dates(block)

        description = "\n".join(lines[1:]) if len(lines) > 1 else block

        experiences.append({
            "job_title": job_title,
            "company": company,
            "start_date": start_date,
            "end_date": end_date,
            "description": description
        })

    return experiences


def format_experiences_as_text(experiences: List[Dict]) -> str:
    parts = []

    for exp in experiences:
        title = exp.get("job_title")
        company = exp.get("company")
        start = exp.get("start_date")
        end = exp.get("end_date")
        description = exp.get("description")

        text_parts = []

        # Title + company
        if title and company:
            text_parts.append(f"{title} at {company}")
        elif title:
            text_parts.append(title)
        elif company:
            text_parts.append(company)

        # Dates
        if start:
            year_part = f"({start.year}"
            if end:
                year_part += f"–{end.year}"
            else:
                year_part += "–Present"
            year_part += ")"
            text_parts.append(year_part)

        # Short description (trimmed)
        if description:
            short_desc = description.strip().replace("\n", " ")
            short_desc = short_desc[:200]  # avoid very long strings
            text_parts.append(f": {short_desc}")

        parts.append(" ".join(text_parts))

    return "; ".join(parts)


def extract_experiences_from_resume(text: str, resume_id: str) -> str:
    """
    Full pipeline: raw text → structured experiences → DB → readable string
    """
    section = extract_experience_section(text)
    experiences = parse_experiences(section)

    if experiences:
        save_experiences_to_db(experiences, resume_id=resume_id)

    experience_text = format_experiences_as_text(experiences)

    return experience_text