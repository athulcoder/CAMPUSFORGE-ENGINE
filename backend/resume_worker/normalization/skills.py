import re

from typing import Set, List

SKILL_MAP = {
    # ---------------- LANGUAGES ----------------
    "python": ["python", "py"],
    "javascript": ["javascript", "js", "ecmascript"],
    "typescript": ["typescript", "ts"],
    "java": ["java"],
    "c": ["c language"],
    "cpp": ["c++"],
    "csharp": ["c#", "c sharp"],
    "go": ["go", "golang"],
    "rust": ["rust"],
    "php": ["php"],
    "ruby": ["ruby"],
    "kotlin": ["kotlin"],
    "swift": ["swift"],
    "dart": ["dart"],
    "scala": ["scala"],
    "r": [" r ", "r language"],

    # ---------------- FRONTEND ----------------
    "react": ["react", "reactjs", "react.js"],
    "nextjs": ["nextjs", "next.js"],
    "vue": ["vue", "vuejs", "vue.js"],
    "angular": ["angular", "angularjs"],
    "html": ["html", "html5"],
    "css": ["css", "css3"],
    "sass": ["sass", "scss"],
    "tailwind": ["tailwind", "tailwindcss"],
    "bootstrap": ["bootstrap"],
    "redux": ["redux"],
    "webpack": ["webpack"],
    "vite": ["vite"],
    "babel": ["babel"],

    # ---------------- BACKEND ----------------
    "nodejs": ["node", "nodejs", "node.js"],
    "express": ["express", "expressjs"],
    "flask": ["flask"],
    "django": ["django"],
    "fastapi": ["fastapi"],
    "spring": ["spring", "spring boot"],
    "nestjs": ["nestjs"],
    "graphql": ["graphql"],
    "restapi": ["rest", "rest api", "restful"],

    # ---------------- DATABASES ----------------
    "postgresql": ["postgres", "postgresql"],
    "mysql": ["mysql"],
    "sqlite": ["sqlite"],
    "mongodb": ["mongodb", "mongo"],
    "redis": ["redis"],
    "elasticsearch": ["elasticsearch", "elastic"],
    "cassandra": ["cassandra"],
    "dynamodb": ["dynamodb"],

    # ---------------- CLOUD ----------------
    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],
    "gcp": ["gcp", "google cloud"],
    "firebase": ["firebase"],
    "vercel": ["vercel"],
    "netlify": ["netlify"],

    # ---------------- DEVOPS ----------------
    "docker": ["docker", "dockerfile"],
    "kubernetes": ["kubernetes", "k8s"],
    "ci_cd": ["ci/cd", "ci cd", "continuous integration"],
    "jenkins": ["jenkins"],
    "github_actions": ["github actions"],
    "terraform": ["terraform"],
    "ansible": ["ansible"],
    "linux": ["linux", "unix"],

    # ---------------- DATA / AI ----------------
    "machine_learning": ["machine learning", "ml"],
    "deep_learning": ["deep learning", "dl"],
    "data_science": ["data science"],
    "data_analysis": ["data analysis"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "scikit_learn": ["scikit-learn", "sklearn"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"],
    "opencv": ["opencv"],
    "nlp": ["nlp", "natural language processing"],

    # ---------------- TESTING ----------------
    "pytest": ["pytest"],
    "jest": ["jest"],
    "selenium": ["selenium"],
    "cypress": ["cypress"],
    "postman": ["postman"],

    # ---------------- MOBILE ----------------
    "android": ["android"],
    "ios": ["ios"],
    "flutter": ["flutter"],
    "react_native": ["react native"],
    "expo": ["expo"],

    # ---------------- TOOLS ----------------
    "git": ["git", "github", "gitlab", "bitbucket"],
    "jira": ["jira"],
    "figma": ["figma"],
    "docker_compose": ["docker compose"],
    "nginx": ["nginx"],
    "apache": ["apache"],

    # ---------------- SECURITY ----------------
    "cybersecurity": ["cybersecurity", "cyber security"],
    "penetration_testing": ["penetration testing", "pentesting"],
    "owasp": ["owasp"],
    "burpsuite": ["burp suite"],
    "wireshark": ["wireshark"],
}

def normalize_skills(raw_skills: List[str]) -> Set[str]:
    """
    Normalize extracted raw skills into canonical skill names.
    Input: ["Python", "React JS", "Node", "Machine Learning"]
    Output: {"python", "react", "node.js", "machine learning"}
    """

    found: Set[str] = set()

    for raw in raw_skills:
        skill = raw.lower().strip()

        # Normalize separators
        skill = re.sub(r"[+/|]", " ", skill)

        # Keep dots for node.js, next.js
        skill = re.sub(r"[^a-z0-9.\s]", " ", skill)
        skill = re.sub(r"\s+", " ", skill).strip()

        for canonical, variants in SKILL_MAP.items():
            for variant in variants:
                v = re.escape(variant.lower())

                # Exact skill match (no partial words)
                pattern = rf"^{v}$"

                if re.match(pattern, skill):
                    found.add(canonical)
                    break

    return found