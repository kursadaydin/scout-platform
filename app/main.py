from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routers import pages

app = FastAPI(title="Scout Platform")

# Template klasörü
templates = Jinja2Templates(directory="app/templates")

# Static dosyalar (css, js)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(pages.router)






