import tempfile
import os

from resume_worker.parsers.pdf_extractor import extract_text_from_pdf
from backend.services.minio_service import download_resume

def parse_resume(job_data):
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        local_path = tmp.name

    download_resume(
        bucket=job_data["bucket"],
        object_name=job_data["object_name"],
        dest=local_path
    )

    text = extract_text_from_pdf(local_path)
    score = basic_score(text)

    os.remove(local_path)
    return text, score


def basic_score(text: str) -> float:
    if not text:
        return 0.0

    keywords = ["python", "java", "react", "sql", "docker"]
    hits = sum(1 for k in keywords if k in text.lower())

    return round((hits / len(keywords)) * 100, 2)