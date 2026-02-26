def score_resume(text: str) -> float:
    """
    Temporary heuristic scoring
    Replace with AI / JD matching later
    """
    if not text:
        return 0.0

    length_score = min(len(text) / 1000, 50)

    keywords = ["python", "react", "sql", "docker", "api"]
    keyword_score = sum(10 for k in keywords if k.lower() in text.lower())

    return round(length_score + keyword_score, 2)