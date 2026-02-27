import re
from backend.resume_worker.extractor.candidate.db_save import saveCandidateToDB


# -------------------- NORMALIZATION --------------------

def normalize_text(text: str) -> str:
    text = text.replace("\u00a0", " ")        # non-breaking spaces
    text = re.sub(r"[ ]{2,}", " ", text)      # multiple spaces
    text = re.sub(r"\n{2,}", "\n", text)      # multiple newlines
    return text.strip()


# -------------------- EMAIL --------------------

def extract_email(text: str) -> str:
    match = re.search(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        text
    )
    return match.group(0) if match else ""


# -------------------- PHONE --------------------

def extract_phone(text: str) -> str:
    text = normalize_text(text)

    # Remove everything except digits and +
    cleaned = re.sub(r"[^\d+]", "", text)

    # Match optional country code + 10 digits
    match = re.search(r"(?:\+?\d{1,3})?\d{10}", cleaned)

    if match:
        return match.group()[-10:]   # last 10 digits only

    return ""


# -------------------- FULL NAME --------------------
def extract_full_name(text: str) -> str:
    text = normalize_text(text)
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    # Explicit section headers (after normalization)
    HARD_REJECT = {
        "details", "skills", "profile", "education", "employment",
        "experience", "languages", "hobbies", "links", "courses",
        "accomplishments", "address", "phone", "email"
    }

    # Only search top of resume (ATS rule)
    search_lines = lines[:7]

    best_candidate = ""
    best_score = -1

    for i, line in enumerate(search_lines):
        # Fix spaced uppercase letters: D E T A I L S → DETAILS
        line = re.sub(r"\b([A-Z])\s+(?=[A-Z]\b)", r"\1", line)

        lower = line.lower()
        words = line.split()

        # Hard rejections
        if lower in HARD_REJECT:
            continue
        if any(h in lower for h in HARD_REJECT):
            continue
        if "@" in line or any(char.isdigit() for char in line):
            continue
        if not (2 <= len(words) <= 3):
            continue

        score = 0

        # Strong positional bias
        if i == 0:
            score += 10
        elif i == 1:
            score += 7
        elif i == 2:
            score += 4

        if line.isupper():
            score += 3
        if len(words) == 2:
            score += 2

        if score > best_score:
            best_score = score
            best_candidate = line

    return best_candidate.title() if best_candidate else ""
# -------------------- LOCATION --------------------

def extract_location(text: str) -> str:
    locations = [
        "thrissur", "alappuzha", "kochi", "ernakulam", "kerala",
        "bangalore", "bengaluru", "chennai", "hyderabad",
        "delhi", "mumbai", "pune", "india","kozhikode","kollam","kannur","goa"
    ]

    text = text.lower()

    for loc in locations:
        if re.search(rf"\b{loc}\b", text):
            return loc.title()

    return ""


# -------------------- MAIN EXTRACTOR --------------------

def extract_candidate(text: str, resume_id: str) -> dict:
    text = normalize_text(text)

    data = {
        "full_name": extract_full_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "location": extract_location(text)
    }

    saveCandidateToDB(data=data, resume_id=resume_id)
    return data