# backend/resume_worker/jobs/job_roles.py

JOB_ROLES = {

    # --------------------------------------------------
    # Core Software Roles
    # --------------------------------------------------

    "Software Engineer": {
        "skills": {
            "core": ["programming", "data structures", "algorithms"],
            "secondary": ["oop", "design patterns"],
            "bonus": ["system design", "testing"]
        },
        "min_experience_years": 1,
        "education_keywords": ["computer science", "engineering"],
        "role_keywords": ["software engineer", "software developer"]
    },

    "Frontend Engineer": {
        "skills": {
            "core": ["javascript", "typescript", "react", "html", "css"],
            "secondary": ["redux", "next.js", "tailwind", "webpack"],
            "bonus": ["vite", "storybook", "jest"]
        },
        "min_experience_years": 1,
        "education_keywords": ["computer science", "engineering", "information technology"],
        "role_keywords": ["frontend engineer", "frontend developer", "ui developer"]
    },

    "Backend Engineer": {
        "skills": {
            "core": ["python", "java", "node.js", "sql", "rest api"],
            "secondary": ["flask", "django", "spring boot", "express"],
            "bonus": ["docker", "postgresql", "redis", "nginx"]
        },
        "min_experience_years": 1,
        "education_keywords": ["computer science", "engineering"],
        "role_keywords": ["backend engineer", "backend developer"]
    },

    "Full Stack Developer": {
        "skills": {
            "core": ["javascript", "react", "node.js", "sql"],
            "secondary": ["next.js", "express", "mongodb"],
            "bonus": ["docker", "git", "aws"]
        },
        "min_experience_years": 2,
        "education_keywords": ["computer science", "engineering"],
        "role_keywords": ["full stack developer", "fullstack engineer"]
    },

    "Product Engineer": {
        "skills": {
            "core": ["product development", "programming"],
            "secondary": ["system design", "databases"],
            "bonus": ["analytics", "user research"]
        },
        "min_experience_years": 2,
        "education_keywords": ["computer science", "engineering"],
        "role_keywords": ["product engineer"]
    },

    # --------------------------------------------------
    # Frontend Specializations
    # --------------------------------------------------

    "React Developer": {
        "skills": {
            "core": ["react", "javascript", "html", "css"],
            "secondary": ["redux", "hooks", "next.js"],
            "bonus": ["vite", "webpack", "jest"]
        },
        "min_experience_years": 1,
        "education_keywords": ["computer science"],
        "role_keywords": ["react developer", "react engineer"]
    },

    "Next.js Developer": {
        "skills": {
            "core": ["next.js", "react", "typescript"],
            "secondary": ["ssr", "seo", "tailwind"],
            "bonus": ["vercel", "vite"]
        },
        "min_experience_years": 1,
        "education_keywords": ["computer science"],
        "role_keywords": ["next.js developer"]
    },

    "UI Engineer": {
        "skills": {
            "core": ["html", "css", "javascript"],
            "secondary": ["accessibility", "responsive design"],
            "bonus": ["animations", "performance optimization"]
        },
        "min_experience_years": 1,
        "education_keywords": ["design", "computer science"],
        "role_keywords": ["ui engineer"]
    },

    "UI/UX Designer": {
        "skills": {
            "core": ["ui design", "ux design", "wireframing"],
            "secondary": ["user research", "prototyping"],
            "bonus": ["figma", "adobe xd"]
        },
        "min_experience_years": 0,
        "education_keywords": ["design", "arts"],
        "role_keywords": ["ui designer", "ux designer"]
    },

    # --------------------------------------------------
    # Backend & Platform
    # --------------------------------------------------

    "Node.js Developer": {
        "skills": {
            "core": ["node.js", "javascript", "express"],
            "secondary": ["mongodb", "postgresql"],
            "bonus": ["docker", "pm2"]
        },
        "min_experience_years": 1,
        "education_keywords": ["computer science"],
        "role_keywords": ["node developer", "node.js engineer"]
    },

    "System Engineer": {
        "skills": {
            "core": ["linux", "networking"],
            "secondary": ["shell scripting"],
            "bonus": ["monitoring", "automation"]
        },
        "min_experience_years": 2,
        "education_keywords": ["computer science", "engineering"],
        "role_keywords": ["system engineer"]
    },

    "Site Reliability Engineer": {
        "skills": {
            "core": ["linux", "monitoring", "incident management"],
            "secondary": ["kubernetes", "cloud"],
            "bonus": ["chaos engineering"]
        },
        "min_experience_years": 2,
        "education_keywords": ["computer science", "engineering"],
        "role_keywords": ["site reliability engineer", "sre"]
    },

    "DevOps Engineer": {
        "skills": {
            "core": ["docker", "kubernetes", "ci/cd"],
            "secondary": ["aws", "linux", "terraform"],
            "bonus": ["jenkins", "github actions"]
        },
        "min_experience_years": 2,
        "education_keywords": ["computer science", "engineering"],
        "role_keywords": ["devops engineer"]
    },

    "Cloud Engineer": {
        "skills": {
            "core": ["aws", "azure", "gcp"],
            "secondary": ["terraform", "linux"],
            "bonus": ["cloudformation"]
        },
        "min_experience_years": 2,
        "education_keywords": ["computer science"],
        "role_keywords": ["cloud engineer"]
    },

    # --------------------------------------------------
    # Data & AI
    # --------------------------------------------------

    "Data Analyst": {
        "skills": {
            "core": ["sql", "data analysis"],
            "secondary": ["excel", "power bi"],
            "bonus": ["python", "tableau"]
        },
        "min_experience_years": 0,
        "education_keywords": ["statistics", "data analytics"],
        "role_keywords": ["data analyst"]
    },

    "Data Scientist": {
        "skills": {
            "core": ["python", "statistics", "data analysis"],
            "secondary": ["pandas", "numpy"],
            "bonus": ["jupyter", "sql"]
        },
        "min_experience_years": 1,
        "education_keywords": ["data science", "statistics"],
        "role_keywords": ["data scientist"]
    },

    "ML Engineer": {
        "skills": {
            "core": ["machine learning", "python"],
            "secondary": ["scikit-learn", "pandas"],
            "bonus": ["mlops", "docker"]
        },
        "min_experience_years": 2,
        "education_keywords": ["computer science", "data science"],
        "role_keywords": ["ml engineer"]
    },

    "AI Engineer": {
        "skills": {
            "core": ["python", "deep learning", "machine learning"],
            "secondary": ["tensorflow", "pytorch"],
            "bonus": ["nlp", "computer vision"]
        },
        "min_experience_years": 2,
        "education_keywords": ["artificial intelligence", "computer science"],
        "role_keywords": ["ai engineer"]
    },

    # --------------------------------------------------
    # Quality & Security
    # --------------------------------------------------

    "QA Engineer": {
        "skills": {
            "core": ["manual testing", "test cases"],
            "secondary": ["automation testing"],
            "bonus": ["selenium", "postman"]
        },
        "min_experience_years": 0,
        "education_keywords": ["computer science"],
        "role_keywords": ["qa engineer", "test engineer"]
    },

    "Automation Engineer": {
        "skills": {
            "core": ["automation testing", "scripting"],
            "secondary": ["selenium", "cypress"],
            "bonus": ["ci/cd"]
        },
        "min_experience_years": 1,
        "education_keywords": ["computer science"],
        "role_keywords": ["automation engineer"]
    },

    "Security Engineer": {
        "skills": {
            "core": ["cybersecurity", "network security"],
            "secondary": ["penetration testing"],
            "bonus": ["burp suite", "wireshark"]
        },
        "min_experience_years": 2,
        "education_keywords": ["cybersecurity", "computer science"],
        "role_keywords": ["security engineer"]
    },

    # --------------------------------------------------
    # Emerging & Specialized
    # --------------------------------------------------

    "Blockchain Developer": {
        "skills": {
            "core": ["blockchain", "smart contracts"],
            "secondary": ["solidity", "ethereum"],
            "bonus": ["web3", "cryptography"]
        },
        "min_experience_years": 1,
        "education_keywords": ["computer science"],
        "role_keywords": ["blockchain developer"]
    },

    "Game Developer": {
        "skills": {
            "core": ["game development", "programming"],
            "secondary": ["unity", "unreal engine"],
            "bonus": ["graphics", "physics"]
        },
        "min_experience_years": 1,
        "education_keywords": ["computer science"],
        "role_keywords": ["game developer"]
    },

    "AR/VR Developer": {
        "skills": {
            "core": ["ar", "vr"],
            "secondary": ["unity", "3d modeling"],
            "bonus": ["c#", "blender"]
        },
        "min_experience_years": 1,
        "education_keywords": ["computer science"],
        "role_keywords": ["ar developer", "vr developer"]
    },

    "Embedded Engineer": {
        "skills": {
            "core": ["embedded systems", "c", "c++"],
            "secondary": ["microcontrollers"],
            "bonus": ["rtos"]
        },
        "min_experience_years": 1,
        "education_keywords": ["electronics", "engineering"],
        "role_keywords": ["embedded engineer"]
    },

    "IoT Engineer": {
        "skills": {
            "core": ["iot", "embedded systems"],
            "secondary": ["mqtt", "sensors"],
            "bonus": ["cloud integration"]
        },
        "min_experience_years": 1,
        "education_keywords": ["electronics", "computer science"],
        "role_keywords": ["iot engineer"]
    },

    # --------------------------------------------------
    # Leadership
    # --------------------------------------------------

    "Tech Lead": {
        "skills": {
            "core": ["system design", "leadership"],
            "secondary": ["code reviews", "mentoring"],
            "bonus": ["architecture"]
        },
        "min_experience_years": 4,
        "education_keywords": ["computer science", "engineering"],
        "role_keywords": ["tech lead"]
    },

    "Engineering Manager": {
        "skills": {
            "core": ["leadership", "system design"],
            "secondary": ["project management", "architecture"],
            "bonus": ["jira", "confluence"]
        },
        "min_experience_years": 5,
        "education_keywords": ["computer science", "engineering"],
        "role_keywords": ["engineering manager", "tech manager"]
    }
}