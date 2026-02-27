from backend.resume_worker.extractor.experience.experience_extraction import extract_experiences_from_resume
from .candidate.candidate_extraction import extract_candidate
from .education.education_extraction import extract_educations_from_resume
def extract_all_and_save_to_db(text:str,resume_id:str):
    extract_candidate(text=text,resume_id=resume_id)
    extract_experiences_from_resume(text=text,resume_id=resume_id)
    extract_educations_from_resume(text,resume_id)