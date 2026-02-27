def score_experience(
    candidate_years: float,
    job_min_years: float
) -> float:
    """
    Scores experience based on how well candidate meets job requirement.
    Returns score in range 0–30.
    """

    MAX_EXP_SCORE = 30.0

    if candidate_years <= 0:
        return 0.0

    if candidate_years >= job_min_years:
        return MAX_EXP_SCORE

    # Partial score if below requirement
    ratio = candidate_years / job_min_years
    return round(ratio * MAX_EXP_SCORE, 2)