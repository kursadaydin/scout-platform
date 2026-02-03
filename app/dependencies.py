from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta

import os
from urllib.parse import urlparse
from fastapi import Request, HTTPException
from dotenv import load_dotenv
from app.core.database import SessionLocal


load_dotenv() 
BASE_URL = os.getenv("BASE_URL")
# BASE_URL → domain çıkar
parsed = urlparse(BASE_URL)
BASE_DOMAIN = parsed.hostname


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =====================================================
# 🔑 API KEY KONTROLÜ (ileride)
# =====================================================

def verify_api_key(request: Request):
    """
    Header'dan API Key kontrolü
    X-API-Key: xxx
    """
    api_key = request.headers.get("X-API-Key")

    # TODO: DB veya ENV'den doğrula
    if not api_key:
        raise HTTPException(
            status_code=403,
            detail="API Key eksik"
        )

    # if api_key not in VALID_KEYS:
    #     raise HTTPException(status_code=403, detail="Geçersiz API Key")

    return api_key


# =====================================================
# ⏱ RATE LIMIT (BASİT TASLAK)
# =====================================================

RATE_LIMIT_STORE = {}

def rate_limit(
    request: Request,
    limit: int = 60,
    window_seconds: int = 60
):
    """
    IP bazlı basit rate limit
    """
    ip = request.client.host
    now = datetime.utcnow()

    data = RATE_LIMIT_STORE.get(ip)

    if not data:
        RATE_LIMIT_STORE[ip] = {
            "count": 1,
            "reset": now + timedelta(seconds=window_seconds)
        }
        return

    if now > data["reset"]:
        RATE_LIMIT_STORE[ip] = {
            "count": 1,
            "reset": now + timedelta(seconds=window_seconds)
        }
        return

    data["count"] += 1

    if data["count"] > limit:
        raise HTTPException(
            status_code=429,
            detail="Çok fazla istek attınız, yavaşlayın"
        )
        
# -------------------------------------------------
# ENV
# -------------------------------------------------
JWT_SECRET = os.getenv("JWT_SECRET", "CHANGE_ME")
JWT_ALGORITHM = "HS256"


# =====================================================
# 🌍 DOMAIN / ORIGIN KONTROLÜ (CORS dışı ek güvenlik)
# =====================================================


def verify_domain(request: Request):
    origin = request.headers.get("origin")

    if not origin:
        return  # browser olmayan isteklerde boş olabilir

    origin_host = urlparse(origin).hostname

    if origin_host != BASE_DOMAIN:
        raise HTTPException(
            status_code=403,
            detail="Bu domain'den erişime izin yok"
        )
        

# -------------------------------------------------
# BEARER TOKEN (JWT) – TASLAK
# -------------------------------------------------
security = HTTPBearer(auto_error=False)

def get_current_user(request: Request):
    user = request.cookies.get("user")

    if not user:
        raise HTTPException(status_code=401)

    return user



    