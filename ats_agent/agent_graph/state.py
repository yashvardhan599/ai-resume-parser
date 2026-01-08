from typing import TypedDict, Dict, Any

class ResumeState(TypedDict, total=False):
    resume_text: str
    jd_text: str
    parsed_resume: Dict[str, Any]
    jd_match: Dict[str, Any]
    score: Dict[str, Any]
    explanation: str