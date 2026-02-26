from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

JOB_DESCRIPTIONS = {
    "backend_developer": """
    Backend developer responsible for APIs, databases,
    authentication, scalability, and server-side logic.
    """
}

def score_semantic(text: str, job_role: str) -> float:
    jd = JOB_DESCRIPTIONS.get(job_role)
    if not jd:
        return 0.0

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([text, jd])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return float(similarity * 20)