import re

MAX_EDU_SCORE = 10.0

# ---------------------------------------------------------
# Education hierarchy (highest wins)
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


def _education_keywords_to_level(keywords: list[str]) -> int:
    """
    Convert job education keywords to required education level (0–4)
    """
    if not keywords:
        return 0

    joined = " ".join(k.lower() for k in keywords)

    for level in sorted(EDUCATION_KEYWORDS.keys(), reverse=True):
        for kw in EDUCATION_KEYWORDS[level]:
            if re.search(rf"\b{re.escape(kw)}\b", joined):
                return level

    return 0


def score_education(
    candidate_level: int,
    job_education_keywords: list[str]
) -> float:
    """
    Scores education using job education keywords.
    Returns score between 0–20.
    """

    required_level = _education_keywords_to_level(job_education_keywords)

    # No education detected in resume
    if candidate_level <= 0:
        return 0.0

    # Job does not specify education → full credit
    if required_level <= 0:
        return MAX_EDU_SCORE

    # Candidate meets or exceeds requirement
    if candidate_level >= required_level:
        return MAX_EDU_SCORE

    # Partial credit
    ratio = candidate_level / required_level
    return round(ratio * MAX_EDU_SCORE, 2)