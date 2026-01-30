from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="/auth")

@router.post("/login")
def login(email: str = Form(...)):
    print("Gelen email:", email)
    return {"ok": True}



@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
    

