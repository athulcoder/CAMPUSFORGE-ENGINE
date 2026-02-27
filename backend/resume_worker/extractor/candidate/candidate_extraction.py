import re
from backend.resume_worker.extractor.candidate.db_save import saveCandidateToDB

def extract_email(text: str) -> str:
    match = re.search(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        text
    )
    return match.group(0) if match else ""

def extract_phone(text: str) -> str:
    match = re.search(
        r"(\+?\d{1,3}[\s-]?)?\b\d{10}\b",
        text
    )
    return match.group(0) if match else ""


def extract_full_name(text: str) -> str:
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    blacklist = [
        "skills", "education", "experience", "projects",
        "summary", "student", "computer", "science"
    ]

    candidates = []

    for line in lines:
        words = line.split()

        if (
            2 <= len(words) <= 4
            and not any(char.isdigit() for char in line)
            and "@" not in line
            and not any(bad in line.lower() for bad in blacklist)
        ):
            # Strong signal if ALL CAPS
            score = 2 if line.isupper() else 1
            candidates.append((score, line))

    if candidates:
        # pick best scored candidate
        candidates.sort(reverse=True)
        return candidates[0][1].title()

    return ""
def extract_location(text: str) -> str:
    common_locations = [
        "kochi", "ernakulam", "kerala", "bangalore",
        "bengaluru", "chennai", "hyderabad", "delhi",
        "mumbai", "pune", "india"
    ]

    for loc in common_locations:
        if loc in text.lower():
            return loc.title()

    return ""


def extract_candidate(text: str,resume_id:str) -> dict:
    text = text.strip()

    data = {
        "full_name": extract_full_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "location": extract_location(text)
    }
    saveCandidateToDB(data=data,resume_id=resume_id);

