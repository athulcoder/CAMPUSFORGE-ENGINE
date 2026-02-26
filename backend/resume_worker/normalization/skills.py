import re

SKILL_MAP = {
    "javascript": ["js", "javascript"],
    "python": ["py", "python"],
    "react": ["react.js", "reactjs"],
    "nodejs": ["node", "node.js"],
    "postgresql": ["postgres", "postgresql"],
}

def normalize_skills(text: str) -> set:
    text = text.lower()
    found = set()

    for canonical, variants in SKILL_MAP.items():
        for v in variants:
            if re.search(rf"\b{v}\b", text):
                found.add(canonical)
                break

    return found