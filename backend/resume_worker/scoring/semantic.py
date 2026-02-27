from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

MAX_SEMANTIC_SCORE = 20.0  # 20% of total score


def score_semantic(resume_text: str, job_description: str) -> float:
    """
    Semantic similarity score using TF-IDF + cosine similarity.

    Inputs:
    - resume_text: full raw resume text
    - job_description: job description text

    Output:
    - score between 0 and 20
    """

    if not resume_text or not job_description:
        return 0.0

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=3000,
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform([
        resume_text.lower(),
        job_description.lower()
    ])

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    # Scale similarity (0–1) → (0–20)
    score = similarity * MAX_SEMANTIC_SCORE

    return round(min(score, MAX_SEMANTIC_SCORE), 2)