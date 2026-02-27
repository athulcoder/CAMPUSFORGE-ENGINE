import re
from typing import Dict, List

from backend.resume_worker.extractor.skills.db_save import saveSkillsToDB
def normalize_text(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ ]{2,}", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()
SKILL_MAP: Dict[str, Dict] = {
    # ---------------- LANGUAGES ----------------
    "python": {"variants": ["python", "py"], "category": "language"},
    "javascript": {"variants": ["javascript", "js"], "category": "language"},
    "typescript": {"variants": ["typescript", "ts"], "category": "language"},
    "java": {"variants": ["java"], "category": "language"},
    "c": {"variants": ["c language"], "category": "language"},
    "cpp": {"variants": ["c++"], "category": "language"},
    "csharp": {"variants": ["c#", "c sharp"], "category": "language"},
    "go": {"variants": ["go", "golang"], "category": "language"},
    "rust": {"variants": ["rust"], "category": "language"},
    "php": {"variants": ["php"], "category": "language"},

    # ---------------- FRONTEND ----------------
    "react": {"variants": ["react", "reactjs", "react.js"], "category": "frontend"},
    "nextjs": {"variants": ["nextjs", "next.js"], "category": "frontend"},
    "vue": {"variants": ["vue", "vuejs"], "category": "frontend"},
    "angular": {"variants": ["angular"], "category": "frontend"},
    "html": {"variants": ["html", "html5"], "category": "frontend"},
    "css": {"variants": ["css", "css3"], "category": "frontend"},
    "tailwind": {"variants": ["tailwind", "tailwindcss"], "category": "frontend"},
    "bootstrap": {"variants": ["bootstrap"], "category": "frontend"},

    # ---------------- BACKEND ----------------
    "nodejs": {"variants": ["nodejs", "node.js"], "category": "backend"},
    "express": {"variants": ["express", "expressjs"], "category": "backend"},
    "flask": {"variants": ["flask"], "category": "backend"},
    "django": {"variants": ["django"], "category": "backend"},
    "fastapi": {"variants": ["fastapi"], "category": "backend"},
    "spring": {"variants": ["spring boot", "spring"], "category": "backend"},

    # ---------------- DATABASE ----------------
    "postgresql": {"variants": ["postgresql", "postgres"], "category": "database"},
    "mysql": {"variants": ["mysql"], "category": "database"},
    "mongodb": {"variants": ["mongodb", "mongo"], "category": "database"},
    "redis": {"variants": ["redis"], "category": "database"},

    # ---------------- DEVOPS ----------------
    "docker": {"variants": ["docker"], "category": "devops"},
    "kubernetes": {"variants": ["kubernetes", "k8s"], "category": "devops"},
    "linux": {"variants": ["linux", "unix"], "category": "devops"},

    # ---------------- DATA / AI ----------------
    "machine_learning": {"variants": ["machine learning"], "category": "data_ai"},
    "deep_learning": {"variants": ["deep learning"], "category": "data_ai"},
    "pandas": {"variants": ["pandas"], "category": "data_ai"},
    "numpy": {"variants": ["numpy"], "category": "data_ai"},
}



_COMPILED_PATTERNS = []

for skill_name, data in SKILL_MAP.items():
    for variant in data["variants"]:
        pattern = re.compile(
            rf"(?<![a-z0-9]){re.escape(variant.lower())}(?![a-z0-9])"
        )
        _COMPILED_PATTERNS.append(
            (pattern, skill_name, data["category"])
        )


def extract_skills(text: str) -> List[Dict[str, str]]:
    text = normalize_text(text).lower()

    # lightweight cleanup
    text = re.sub(r"[|,/+]", " ", text)
    text = re.sub(r"[^a-z0-9.\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    found = {}

    for pattern, skill_name, category in _COMPILED_PATTERNS:
        if pattern.search(text):
            found[skill_name] = category

    return [
        {
            "skill_name": skill,
            "category": category
        }
        for skill, category in found.items()
    ]



def extract_skills_from_resume(text: str, resume_id: str) -> List[Dict[str, str]]:
    """
    Extract skills from resume text and save them to DB
    """
    skills = extract_skills(text)

    if skills:
        saveSkillsToDB(
            data=skills,
            resume_id=resume_id
        )
    skill_names = [s["skill_name"] for s in skills]
    return skill_names