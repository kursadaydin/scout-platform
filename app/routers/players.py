from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.dependencies import get_current_user



router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/{player_id}", response_class=HTMLResponse)
def player_detail(
    player_id: int,
    request: Request,
    user: str = Depends(get_current_user)
):
    # ŞİMDİLİK MOCK DATA (sonra DB’den gelecek)
    player = {
        "id": player_id,
        "name": "Victor Boniface",
        "position": "ST",
        "nationality": "Nigeria",
        "age": 23,
        "height": 190,
        "foot": "Right",
        "team": "Leverkusen",
        "league": "Bundesliga"
    }

    stats = [
        {
            "season": "2023/24",
            "minutes": 2100,
            "goals": 14,
            "assists": 6,
            "xg": 12.4
        }
    ]

    return templates.TemplateResponse(
        "player_detail.html",
        {
            "request": request,
            "user": user,
            "player": player,
            "stats": stats
        }
    )