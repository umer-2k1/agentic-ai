from dataclasses import dataclass
from typing import List, Optional

@dataclass
class JobDescription:
    title: str
    department: str
    requirements: List[str]
    preferred_skills: List[str]
    experience_level: str
    description: str
    posted_date: str

@dataclass
class Candidate:
    name: str
    email: str
    phone: str
    resume_path: str
    extracted_text: str = ""
    skills: List[str] = None
    experience_years: int = 0
    education: str = ""
    status: str = "pending"
    score: float = 0.0
    evaluation_notes: str = ""
    interview_scheduled: Optional[str] = None

@dataclass
class RecruitmentReport:
    job_title: str
    total_candidates: int
    shortlisted_count: int
    rejected_count: int
    pending_count: int
    avg_score: float
    top_candidates: List[str]
    generated_date: str
