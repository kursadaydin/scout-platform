import random
from datetime import datetime, timedelta
import secrets
from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse, JSONResponse
from app.services.email import send_otp_email

from fastapi import APIRouter, Form, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.responses import JSONResponse

from app.core.database import SessionLocal
from app.models.user import User

from app.dependencies import get_db


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

    try:
        send_otp_email(email, code)
    except Exception as e:
        print("RESEND ERROR:", e)

        # 🔴 500 yerine kontrollü cevap
        raise HTTPException(
            status_code=400,
            detail="Mail gönderilemedi (Resend)"
        )

    return {
        "message": "OTP gönderildi",
        "expires_in": 300
    }

# -------------------------
# OTP DOĞRULA
# -------------------------
@router.post("/verify")
def verify_code( request: Request,
    email: str = Form(...),
    code: str = Form(...),
    db: Session = Depends(get_db)
):
    data = OTP_STORE.get(email)

    if not data:
        raise HTTPException(status_code=400, detail="Kod bulunamadı")

    if datetime.utcnow() > data["expires"]:
        raise HTTPException(status_code=400, detail="Kod süresi doldu")

    if data["code"] != code:
        raise HTTPException(status_code=400, detail="Kod hatalı")
    
    request.session["user"] = email

   # kullanıcı DB'de yoksa ekleme
    user = db.query(User).filter(User.email == email).first()
    if not user:
        user = User(email=email)
        db.add(user)
        db.commit()
        db.refresh(user)

    # 🔹 Son login tarihini güncelle
    user.last_login = datetime.utcnow()
    db.commit()
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
