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
        <div style="font-family:Arial,sans-serif; padding:20px; background:#f4f6f8;">
            <div style="max-width:400px; margin:auto; background:#fff; padding:24px; border-radius:8px; text-align:center;">
                <h2 style="color:#111827; margin-bottom:16px;">Scout Platform</h2>
                <p style="color:#6b7280; margin-bottom:24px;">Giriş yapmak için aşağıdaki kodu kullan:</p>
                <div style="font-size:32px; font-weight:700; letter-spacing:6px; color:#111827; margin-bottom:24px; border:1px dashed #d1d5db; padding:16px; border-radius:6px;">
                    {code}
                </div>
                <p style="color:#374151; font-size:14px; margin-bottom:12px;">Kod <strong>5 dakika</strong> geçerlidir.</p>
                <p style="color:#9ca3af; font-size:12px; margin:0;">Eğer bu isteği sen yapmadıysan, bu e-postayı yok sayabilirsin.</p>
            </div>
        </div>
        """
    })
