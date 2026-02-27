from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def tfidf_similarity(a: str, b: str) -> float:
    if not a or not b:
        return 0.0

    vec = TfidfVectorizer(
        stop_words="english",
        max_features=3000,
        ngram_range=(1, 2),
        sublinear_tf=True
    )
    tfidf = vec.fit_transform([a, b])
    return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]


def score_semantic(resume_sem: dict, role_sem: dict) -> float:
    skill_sim = tfidf_similarity(resume_sem["skills"], role_sem["skills"])
    title_sim = tfidf_similarity(resume_sem["titles"], role_sem["keywords"])
    desc_sim  = tfidf_similarity(resume_sem["content"], role_sem["description"])

    # weights tuned for hiring relevance
    combined = (
        0.5 * skill_sim +
        0.3 * title_sim +
        0.2 * desc_sim
    )

    # non-linear boost (critical)
    score = (combined ** 0.5) * 20

    return round(min(score, 20.0), 2)