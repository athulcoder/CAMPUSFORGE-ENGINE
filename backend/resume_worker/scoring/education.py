def score_education(text: str) -> float:
    t = text.lower()

    if "bachelor" in t or "b.tech" in t:
        return 8
    if "master" in t or "m.tech" in t:
        return 10
    if "diploma" in t:
        return 5
    return 2