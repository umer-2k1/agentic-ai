from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
import json
from langchain_core.output_parsers import JsonOutputParser



class LLMEvaluator:
    def __init__(self, api_key: str):
        self.llm = ChatGroq(
            groq_api_key=api_key,
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            temperature=0.3,
        )
        
        self.output_parser = JsonOutputParser()

    def evaluate_candidate(self, candidate, job_desc):
        prompt = f"""
        Evaluate this candidate for the position: {job_desc.title}

        Job Requirements:
        - {'\n- '.join(job_desc.requirements)}

        Preferred Skills:
        - {'\n- '.join(job_desc.preferred_skills)}

        Candidate Resume:
        {candidate.extracted_text}
        
        
        Return this **exact JSON** format:
        {{
            "score": <number>,
            "status": "<shortlisted/rejected/needs review>",
            "skills_match": [<list of strings>],
            "experience_years": <float>,
            "education": "<string>",
            "evaluation_notes": [<list of bullet points or a paragraph as string>]
          
        }}

        """
        print("prompt....", prompt)
        messages = [
            (
                "system",
                "You are an expert technical recruiter. Evaluate the candidate based on job requirements.",
            ),
            ("human", prompt)
        ]
        try:
            response = self.llm.invoke(messages)
            parse_result = self.output_parser.parse(response.content)
            print("RAW RESPONSE:", parse_result)
            # print("LLM.............", parse_result)
            return parse_result
        except Exception as e:
            import traceback
            print(traceback.print_exc())
            print(f"LLM error: {e}")
            return {
                "score": 0,
                "status": "rejected",
                "skills_match": [],
                "experience_years": 0,
                "education": "Unknown",
                "evaluation_notes": "Error",
            }
