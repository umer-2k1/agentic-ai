import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_FROM = os.getenv("MAIL_FROM") 


EMAIL_CONFIG = {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "email": MAIL_FROM,
    "password": MAIL_PASSWORD
}

GROQ_API_KEY =GROQ_API_KEY
