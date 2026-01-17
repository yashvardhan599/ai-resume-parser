from pydantic import BaseModel
from typing import List, Optional

from core.llm import llm

class ParsedResume(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    total_experience_years: Optional[float]
    skills: List[str]
    education: List[str]
    companies: List[str]


class JDMatch(BaseModel):
    matched_skills: List[str]
    missing_skills: List[str]
    experience_fit: str
    domain_fit: str


class CandidateScore(BaseModel):
    final_score: int
    category: str
    reasoning: str

resume_parser_llm = llm.with_structured_output(ParsedResume)
jd_matcher_llm = llm.with_structured_output(JDMatch)
scorer_llm = llm.with_structured_output(CandidateScore)