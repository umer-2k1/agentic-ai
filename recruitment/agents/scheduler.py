from datetime import datetime, timedelta


class InterviewScheduler:
    def schedule_interview(self):
        date = datetime.now() + timedelta(days=7)
        time = date.strftime("%Y-%m-%d at 2:00 PM")
        return time
