# backend/resume_worker/jobs/job_roles.py

JOB_ROLES = {

    # --------------------------------------------------
    # Core Software Roles
    # --------------------------------------------------

    "Software Engineer": {
        "job_description": "Builds and maintains software applications using strong programming fundamentals. Works closely with teams to design, develop, and improve scalable solutions.",
        "skills": {
            "core": ["programming", "data structures", "algorithms"],
            "secondary": ["oop", "design patterns"],
            "bonus": ["system design", "testing"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "computer science", "engineering",
            "bachelor", "b.tech", "btech", "be",
            "m.tech", "mtech", "diploma"
        ],
        "role_keywords": ["software engineer", "software developer"]
    },

    "Frontend Engineer": {
        "job_description": "Develops user-facing features with a focus on performance and usability. Collaborates with designers and backend teams to deliver seamless web experiences.",
        "skills": {
            "core": ["javascript", "typescript", "react", "html", "css"],
            "secondary": ["redux", "next.js", "tailwind", "webpack"],
            "bonus": ["vite", "storybook", "jest"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "computer science", "engineering", "information technology",
            "bachelor", "b.tech", "btech", "be", "diploma"
        ],
        "role_keywords": ["frontend engineer", "frontend developer", "ui developer"]
    },

    "Backend Engineer": {
        "job_description": "Designs and implements server-side logic, APIs, and databases. Ensures scalability, security, and performance of backend systems.",
        "skills": {
            "core": ["python", "java", "node.js", "sql", "rest api"],
            "secondary": ["flask", "django", "spring boot", "express"],
            "bonus": ["docker", "postgresql", "redis", "nginx"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "computer science", "engineering",
            "bachelor", "b.tech", "btech", "be",
            "m.tech", "mtech"
        ],
        "role_keywords": ["backend engineer", "backend developer"]
    },

    "Full Stack Developer": {
        "job_description": "Works on both frontend and backend components of applications. Handles end-to-end development and integration of features.",
        "skills": {
            "core": ["javascript", "react", "node.js", "sql"],
            "secondary": ["next.js", "express", "mongodb"],
            "bonus": ["docker", "git", "aws"]
        },
        "min_experience_years": 2,
        "education_keywords": [
            "computer science", "engineering",
            "bachelor", "b.tech", "btech", "be"
        ],
        "role_keywords": ["full stack developer", "fullstack engineer"]
    },

    "Product Engineer": {
        "job_description": "Builds products with a strong focus on user needs and business goals. Collaborates with stakeholders to deliver impactful features.",
        "skills": {
            "core": ["product development", "programming"],
            "secondary": ["system design", "databases"],
            "bonus": ["analytics", "user research"]
        },
        "min_experience_years": 2,
        "education_keywords": [
            "computer science", "engineering",
            "bachelor", "b.tech", "m.tech"
        ],
        "role_keywords": ["product engineer"]
    },

    # --------------------------------------------------
    # Frontend Specializations
    # --------------------------------------------------

    "React Developer": {
        "job_description": "Develops dynamic user interfaces using React and modern JavaScript. Focuses on component-based architecture and performance optimization.",
        "skills": {
            "core": ["react", "javascript", "html", "css"],
            "secondary": ["redux", "hooks", "next.js"],
            "bonus": ["vite", "webpack", "jest"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "computer science",
            "bachelor", "b.tech", "btech", "diploma"
        ],
        "role_keywords": ["react developer", "react engineer"]
    },

    "Next.js Developer": {
        "job_description": "Builds scalable web applications using Next.js and React. Optimizes applications for SEO, performance, and server-side rendering.",
        "skills": {
            "core": ["next.js", "react", "typescript"],
            "secondary": ["ssr", "seo", "tailwind"],
            "bonus": ["vercel", "vite"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "computer science",
            "bachelor", "b.tech", "btech"
        ],
        "role_keywords": ["next.js developer"]
    },

    "UI Engineer": {
        "job_description": "Implements clean and accessible user interfaces using web technologies. Ensures responsive design across different devices and platforms.",
        "skills": {
            "core": ["html", "css", "javascript"],
            "secondary": ["accessibility", "responsive design"],
            "bonus": ["animations", "performance optimization"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "design", "computer science",
            "bachelor", "diploma"
        ],
        "role_keywords": ["ui engineer"]
    },

    "UI/UX Designer": {
        "job_description": "Designs intuitive and engaging user experiences for digital products. Conducts research and creates wireframes and prototypes.",
        "skills": {
            "core": ["ui design", "ux design", "wireframing"],
            "secondary": ["user research", "prototyping"],
            "bonus": ["figma", "adobe xd"]
        },
        "min_experience_years": 0,
        "education_keywords": [
            "design", "arts",
            "bachelor", "diploma"
        ],
        "role_keywords": ["ui designer", "ux designer"]
    },

    # --------------------------------------------------
    # Backend & Platform
    # --------------------------------------------------

    "Node.js Developer": {
        "job_description": "Develops backend services using Node.js and JavaScript. Builds APIs and ensures efficient server-side performance.",
        "skills": {
            "core": ["node.js", "javascript", "express"],
            "secondary": ["mongodb", "postgresql"],
            "bonus": ["docker", "pm2"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "computer science",
            "bachelor", "b.tech", "btech"
        ],
        "role_keywords": ["node developer", "node.js engineer"]
    },

    "System Engineer": {
        "job_description": "Manages and maintains system infrastructure and servers. Ensures system reliability, performance, and security.",
        "skills": {
            "core": ["linux", "networking"],
            "secondary": ["shell scripting"],
            "bonus": ["monitoring", "automation"]
        },
        "min_experience_years": 2,
        "education_keywords": [
            "computer science", "engineering",
            "b.tech", "diploma"
        ],
        "role_keywords": ["system engineer"]
    },

    "Site Reliability Engineer": {
        "job_description": "Ensures high availability and reliability of production systems. Uses monitoring and automation to prevent and resolve incidents.",
        "skills": {
            "core": ["linux", "monitoring", "incident management"],
            "secondary": ["kubernetes", "cloud"],
            "bonus": ["chaos engineering"]
        },
        "min_experience_years": 2,
        "education_keywords": [
            "computer science", "engineering",
            "b.tech", "m.tech"
        ],
        "role_keywords": ["site reliability engineer", "sre"]
    },

    "DevOps Engineer": {
        "job_description": "Automates deployment pipelines and manages cloud infrastructure. Bridges development and operations for faster delivery.",
        "skills": {
            "core": ["docker", "kubernetes", "ci/cd"],
            "secondary": ["aws", "linux", "terraform"],
            "bonus": ["jenkins", "github actions"]
        },
        "min_experience_years": 2,
        "education_keywords": [
            "computer science", "engineering",
            "b.tech", "m.tech"
        ],
        "role_keywords": ["devops engineer"]
    },

    "Cloud Engineer": {
        "job_description": "Designs and manages cloud-based infrastructure and services. Ensures scalability, security, and cost efficiency.",
        "skills": {
            "core": ["aws", "azure", "gcp"],
            "secondary": ["terraform", "linux"],
            "bonus": ["cloudformation"]
        },
        "min_experience_years": 2,
        "education_keywords": [
            "computer science",
            "b.tech", "m.tech"
        ],
        "role_keywords": ["cloud engineer"]
    },

    # --------------------------------------------------
    # Data & AI
    # --------------------------------------------------

    "Data Analyst": {
        "job_description": "Analyzes data to generate insights and support decision making. Creates reports and dashboards for stakeholders.",
        "skills": {
            "core": ["sql", "data analysis"],
            "secondary": ["excel", "power bi"],
            "bonus": ["python", "tableau"]
        },
        "min_experience_years": 0,
        "education_keywords": [
            "statistics", "data analytics",
            "bachelor", "diploma"
        ],
        "role_keywords": ["data analyst"]
    },

    "Data Scientist": {
        "job_description": "Uses data to build predictive models and extract insights. Applies statistical and machine learning techniques.",
        "skills": {
            "core": ["python", "statistics", "data analysis"],
            "secondary": ["pandas", "numpy"],
            "bonus": ["jupyter", "sql"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "data science", "statistics",
            "bachelor", "m.sc", "msc"
        ],
        "role_keywords": ["data scientist"]
    },

    "ML Engineer": {
        "job_description": "Builds and deploys machine learning models into production. Works closely with data scientists and engineers.",
        "skills": {
            "core": ["machine learning", "python"],
            "secondary": ["scikit-learn", "pandas"],
            "bonus": ["mlops", "docker"]
        },
        "min_experience_years": 2,
        "education_keywords": [
            "computer science", "data science",
            "b.tech", "m.tech"
        ],
        "role_keywords": ["ml engineer"]
    },

    "AI Engineer": {
        "job_description": "Develops intelligent systems using machine learning and deep learning. Applies AI techniques to solve real-world problems.",
        "skills": {
            "core": ["python", "deep learning", "machine learning"],
            "secondary": ["tensorflow", "pytorch"],
            "bonus": ["nlp", "computer vision"]
        },
        "min_experience_years": 2,
        "education_keywords": [
            "artificial intelligence", "computer science",
            "b.tech", "m.tech"
        ],
        "role_keywords": ["ai engineer"]
    },

    # --------------------------------------------------
    # Quality & Security
    # --------------------------------------------------

    "QA Engineer": {
        "job_description": "Ensures software quality through manual and automated testing. Identifies bugs and improves product reliability.",
        "skills": {
            "core": ["manual testing", "test cases"],
            "secondary": ["automation testing"],
            "bonus": ["selenium", "postman"]
        },
        "min_experience_years": 0,
        "education_keywords": [
            "computer science",
            "bachelor", "diploma"
        ],
        "role_keywords": ["qa engineer", "test engineer"]
    },

    "Automation Engineer": {
        "job_description": "Builds automated test frameworks and scripts. Improves testing efficiency and coverage.",
        "skills": {
            "core": ["automation testing", "scripting"],
            "secondary": ["selenium", "cypress"],
            "bonus": ["ci/cd"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "computer science",
            "b.tech", "bachelor"
        ],
        "role_keywords": ["automation engineer"]
    },

    "Security Engineer": {
        "job_description": "Protects systems and applications from security threats. Conducts assessments and implements security controls.",
        "skills": {
            "core": ["cybersecurity", "network security"],
            "secondary": ["penetration testing"],
            "bonus": ["burp suite", "wireshark"]
        },
        "min_experience_years": 2,
        "education_keywords": [
            "cybersecurity", "computer science",
            "b.tech", "m.tech"
        ],
        "role_keywords": ["security engineer"]
    },

    # --------------------------------------------------
    # Emerging & Specialized
    # --------------------------------------------------

    "Blockchain Developer": {
        "job_description": "Develops decentralized applications using blockchain technology. Writes and deploys smart contracts securely.",
        "skills": {
            "core": ["blockchain", "smart contracts"],
            "secondary": ["solidity", "ethereum"],
            "bonus": ["web3", "cryptography"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "computer science",
            "b.tech", "bachelor"
        ],
        "role_keywords": ["blockchain developer"]
    },

    "Game Developer": {
        "job_description": "Designs and builds interactive games and game mechanics. Works with graphics, physics, and gameplay logic.",
        "skills": {
            "core": ["game development", "programming"],
            "secondary": ["unity", "unreal engine"],
            "bonus": ["graphics", "physics"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "computer science",
            "bachelor", "diploma"
        ],
        "role_keywords": ["game developer"]
    },

    "AR/VR Developer": {
        "job_description": "Creates immersive augmented and virtual reality experiences. Develops interactive 3D environments and applications.",
        "skills": {
            "core": ["ar", "vr"],
            "secondary": ["unity", "3d modeling"],
            "bonus": ["c#", "blender"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "computer science",
            "bachelor", "diploma"
        ],
        "role_keywords": ["ar developer", "vr developer"]
    },

    "Embedded Engineer": {
        "job_description": "Develops software for embedded and hardware-based systems. Works closely with electronics and firmware components.",
        "skills": {
            "core": ["embedded systems", "c", "c++"],
            "secondary": ["microcontrollers"],
            "bonus": ["rtos"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "electronics", "engineering",
            "diploma", "b.tech"
        ],
        "role_keywords": ["embedded engineer"]
    },

    "IoT Engineer": {
        "job_description": "Builds connected devices and IoT solutions. Integrates hardware, software, and cloud services.",
        "skills": {
            "core": ["iot", "embedded systems"],
            "secondary": ["mqtt", "sensors"],
            "bonus": ["cloud integration"]
        },
        "min_experience_years": 1,
        "education_keywords": [
            "electronics", "computer science",
            "diploma", "b.tech"
        ],
        "role_keywords": ["iot engineer"]
    },

    # --------------------------------------------------
    # Leadership
    # --------------------------------------------------

    "Tech Lead": {
        "job_description": "Leads technical teams and designs system architecture. Guides developers and ensures code quality.",
        "skills": {
            "core": ["system design", "leadership"],
            "secondary": ["code reviews", "mentoring"],
            "bonus": ["architecture"]
        },
        "min_experience_years": 4,
        "education_keywords": [
            "computer science", "engineering",
            "b.tech", "m.tech"
        ],
        "role_keywords": ["tech lead"]
    },

    "Engineering Manager": {
        "job_description": "Manages engineering teams and project execution. Balances technical decisions with business goals.",
        "skills": {
            "core": ["leadership", "system design"],
            "secondary": ["project management", "architecture"],
            "bonus": ["jira", "confluence"]
        },
        "min_experience_years": 5,
        "education_keywords": [
            "computer science", "engineering",
            "b.tech", "m.tech", "mba"
        ],
        "role_keywords": ["engineering manager", "tech manager"]
    }
}