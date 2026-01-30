import secrets
from fastapi import APIRouter
from app.services.email import send_login_email

router = APIRouter(prefix="/auth", tags=["auth"])

# geçici hafıza (şimdilik DB yok)
TOKENS = {}

@router.post("/login")
def login(email: str):
    token = secrets.token_urlsafe(32)

    TOKENS[token] = email
    
    
    try:
        send_login_email(email, token)
    except Exception as e:
        print("MAIL ERROR:", e)

    

    return {"message": "Giriş linki email adresinize gönderildi."}


@router.get("/verify/{token}")
def verify(token: str):
    
    email = TOKENS.get(token)
    if not email:
        return {"error": "Geçersiz token"}

    return {"message": f"{email} giriş yaptı"}