from backend.resume_worker.extractions.experience.experience_extraction import extract_experiences_from_resume
from .candidate.candidate_extraction import extract_candidate
def extract_all_and_save_to_db(text:str,resume_id:str):
    extract_candidate(text=text,resume_id=resume_id)
    extract_experiences_from_resume(text=text,resume_id=resume_id)