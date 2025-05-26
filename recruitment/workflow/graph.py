from langgraph.graph import Graph, END

class RecruitmentWorkflow:
    def __init__(self, extractor, evaluator, scheduler, notifier=None):
        self.extractor = extractor
        self.evaluator = evaluator
        self.scheduler = scheduler
        self.notifier = notifier
        self.job_desc = None
        self.candidates = []
        self.workflow = self._build_workflow()
        
    def _build_workflow(self):
        graph = Graph()
        graph.add_node("extract_resume", self._extract_resume)
        graph.add_node("evaluate", self._evaluate)
        graph.add_node("notify", self._notify)
        graph.add_node("schedule", self._schedule)
        
        graph.add_edge("extract_resume", "evaluate")
        graph.add_conditional_edges("evaluate", self._route, {
            "rejected": "notify",
            "shortlisted": "schedule"
        })
        graph.add_edge("notify", END)
        graph.add_edge("schedule", END)
        graph.set_entry_point("extract_resume")
        return graph.compile()
        
        
    
    def set_job_description(self, job_desc):
        self.job_desc = job_desc
        
    def _extract_resume(self, state):
        c = state["candidate"]
        c.extracted_text = self.extractor.extract_text(c.resume_path)
        return {"candidate": c}
    
    def _evaluate(self, state):
        c = state["candidate"]
        eval_result =  self.evaluator.evaluate_candidate(c,self.job_desc) 
        c.score = eval_result["score"]
        c.status = eval_result["status"]
        c.skills = eval_result["skills_match"]
        c.experience_years = eval_result["experience_years"]
        c.education = eval_result["education"]
        c.evaluation_notes = eval_result["evaluation_notes"]
        return {"candidate": c}
    
    def _route(self, state):
        return state["candidate"].status
    
    def _notify(self, state):
        c = state["candidate"]
        if self.notifier:
            self.notifier.send_rejection_email(c, self.job_desc.title)
        return {"candidate": c}
    
    def _schedule(self, state):
        c = state["candidate"]
        date = self.scheduler.schedule_interview(c)
        c.interview_scheduled = date
        if self.notifier:
            self.notifier.send_interview_email(c, self.job_desc.title, date)
        return {"candidate": c}
            
            
    def run(self, candidate):
        result  = self.workflow.invoke({"candidate": candidate})
        self.candidates.append(result["candidate"])
        return result["candidate"]
        
                
            
        
        

