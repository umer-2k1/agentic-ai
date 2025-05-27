from models import JobDescription, Candidate
from config import EMAIL_CONFIG, GROQ_API_KEY
from agents.pdf_extractor import PDFExtractor
from agents.llm_evaluator import LLMEvaluator
from agents.notifier import EmailNotifier
from agents.scheduler import InterviewScheduler
from workflow.graph import RecruitmentWorkflow


def main():
    jd = JobDescription(
        title="Ai Software Engineer",
        department="Engineering",
        # description="React Native, Next js and AI project experience preferred.",
        description="Generative AI, LLMs, LangChain, Groq, Git",
        experience_level="Mid-Level",
        requirements=["Machine Learning Engineer", "Generative Ai", "AI Developer"],
        # requirements=["Typescript", "Node Js", "Git"],
        preferred_skills=["LangChain", "Groq", "LLMs"],
        # preferred_skills=["Groq", "LLMs"],
        # preferred_skills=["Web application", "Mobile Development", "LLMs"],
        posted_date="2025-01-01",
    )

    # sample candidate
    candidate = Candidate(
        name="Muhammad Umer",
        email="memonumer504@gmail.com",
        phone="1234567890",
        resume_path="resumes/umer-resume.pdf",
    )

    # Workflow
    workflow = RecruitmentWorkflow(
        extractor=PDFExtractor(),
        evaluator=LLMEvaluator(GROQ_API_KEY),
        scheduler=InterviewScheduler(),
        notifier=EmailNotifier(**EMAIL_CONFIG),
    )

    workflow.set_job_description(jd)
    proceed = workflow.run(candidate=candidate)

    print(f"Candidate {proceed.name} Status: {proceed.status}, Score: {proceed.score}")


if __name__ == "__main__":
    main()
