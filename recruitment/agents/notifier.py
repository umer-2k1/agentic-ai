import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailNotifier:
    def __init__(self, smtp_server, smtp_port, email, password):
        print("EMaill", smtp_server, smtp_port, email, password)
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password
        
    def _send_email(self, to_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        print("slef..." ,self.email, self.password, self.smtp_server, self.smtp_port)

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            import traceback
            print(traceback.print_exc())
            print(f"Email error: {e}")
            
    def send_rejection_email(self, candidate, job_title):
        body = f"""
        Dear {candidate.name},

        Thank you for applying for the {job_title} position. Unfortunately, we have decided to proceed with other candidates.

        Best regards,
        HR Team
        """
        self._send_email(candidate.email, f"Update - {job_title}", body)
        
    def send_interview_email(self, candidate, job_title, date):
        body = f"""
        Dear {candidate.name},

        Congratulations! You're shortlisted for {job_title}. Your interview is scheduled on {date}.

        Best regards,
        HR Team
        """
        self._send_email(candidate.email, f"Interview - {job_title}", body)