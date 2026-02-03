import resend
import os
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")
BASE_URL = os.getenv("BASE_URL")


def send_login_email(email: str, token: str):
    login_link = f"{BASE_URL}/auth/verify/{token}"

    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": [email],
        "subject": "Scout Platform giriş linkiniz",
        "html": f"""
            <h2>Giriş Linki</h2>
            <p>Giriş yapmak için aşağıdaki linke tıklayın:</p>
            <a href="{login_link}">{login_link}</a>
        """
    })
    
def send_otp_email(email: str, code: str):
    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": [email],
        "subject": "Giriş Kodun",
        "html": f"""
        <h2>Scout Platform</h2>
        <p>Giriş kodun:</p>
        <h1 style="letter-spacing:6px">{code}</h1>
        <p>5 dakika geçerlidir.</p>
        """
    })
