# Replace with SQLAlchemy later

def get_candidate_full(candidate_id):
    # simulate DB record
    return {
        "id": candidate_id,
        "name": "Arjun Menon",
        "role": "Frontend Engineer",
        "score": 92,
        "skills": ["React", "TypeScript", "Tailwind"],
        "experience": "3 years",
        "resume_text": "Full resume content...",
        "ai_analysis": {
            "strengths": ["UI design", "Performance"],
            "weaknesses": ["Backend depth"]
        }
    }