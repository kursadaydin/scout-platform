from fastapi import APIRouter, Request, Depends, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.models.player_stats import PlayerStats
from app.dependencies import get_db, get_current_user

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

@router.get("/")
def index(
    request: Request,
    name: str | None = None,
    db: Session = Depends(get_db),
    user: str | None = Depends(get_current_user)  # 👈 opsiyonel
):
    players = []
    if name:
        players = (
            db.query(PlayerStats)
            .filter(PlayerStats.player == name)
            .all()
        )

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "players": players,
            "user": user,   # 🔥 navbar için
        }
    )