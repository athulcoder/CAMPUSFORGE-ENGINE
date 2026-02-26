import re

def extract_years(text: str) -> float:
    matches = re.findall(r"(\d+)\+?\s+years?", text.lower())
    return max(map(int, matches), default=0)

def score_experience(text: str) -> float:
    years = extract_years(text)

    if years >= 5:
        return 30
    if years >= 3:
        return 22
    if years >= 1:
        return 15
    return 5