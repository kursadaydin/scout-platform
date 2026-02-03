from fastapi import APIRouter, Request, Depends, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.models.player_stats import PlayerStats
from app.dependencies import get_db

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

@router.get("/", response_class=HTMLResponse)
def home(request: Request, name: str = Query(None), db: Session = Depends(get_db)):
    player_data = []

    if name:
        # Oyuncu adına göre tüm sezonları getir
        player_data = db.query(PlayerStats).filter(PlayerStats.player.ilike(f"%{name}%")).order_by(PlayerStats.season.desc()).all()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "players": player_data
        }
    )