from fastapi import APIRouter, Request, Depends, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.dependencies import get_current_user

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

@router.get("/", response_class=HTMLResponse)
def home(
    request: Request,
    user: str = Depends(get_current_user)
):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "user": user
        }
    )
