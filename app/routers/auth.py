import random
from datetime import datetime, timedelta
import secrets
from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse, JSONResponse
from app.services.email import send_otp_email

router = APIRouter(prefix="/auth", tags=["auth"])

OTP_STORE = {}

import random
from datetime import datetime, timedelta
from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import RedirectResponse
from app.services.email import send_otp_email

router = APIRouter(prefix="/auth", tags=["auth"])

OTP_STORE = {}

# -------------------------
# OTP GÖNDER
# -------------------------
@router.post("/send")
def send_code(email: str = Form(...)):
    code = str(random.randint(100000, 999999))
    expires = datetime.utcnow() + timedelta(minutes=5)

    OTP_STORE[email] = {
        "code": code,
        "expires": expires
    }

    send_otp_email(email, code)

    # 🔑 ARTIK REDIRECT YOK
    return {
        "message": "OTP gönderildi",
        "expires_in": 300
    }


# -------------------------
# OTP DOĞRULA
# -------------------------
@router.post("/verify")
def verify_code(
    email: str = Form(...),
    code: str = Form(...)
):
    data = OTP_STORE.get(email)

    if not data:
        raise HTTPException(status_code=400, detail="Kod bulunamadı")

    if datetime.utcnow() > data["expires"]:
        raise HTTPException(status_code=400, detail="Kod süresi doldu")

    if data["code"] != code:
        raise HTTPException(status_code=400, detail="Kod hatalı")

    del OTP_STORE[email]

    response = JSONResponse({"success": True})
    response.set_cookie(
        key="user",
        value=email,
        httponly=True,
        samesite="lax"
    )

    return response


# -------------------------
# LOGOUT
# -------------------------
@router.get("/logout")
def logout():
    response = RedirectResponse("/login", status_code=302)
    response.delete_cookie("user")
    return response
