from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.player_stats import PlayerStats  # SQLAlchemy Player modeli
from app.dependencies import verify_domain, rate_limit

router = APIRouter(prefix="/api")

@router.get("/players/autocomplete", dependencies=[
        Depends(verify_domain),
        Depends(rate_limit)
    ])
def player_autocomplete(
    q: str = Query(..., min_length=3),
    db: Session = Depends(get_db)
):
    results = (
        db.query(PlayerStats.player)
        .filter(PlayerStats.player.ilike(f"%{q}%"))
        .group_by(PlayerStats.player)
        .order_by(PlayerStats.player)
        .limit(10)
        .all()
    )

    return [r.player for r in results]