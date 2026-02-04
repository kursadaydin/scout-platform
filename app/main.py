
import truststore
truststore.inject_into_ssl()
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os

from starlette.middleware.sessions import SessionMiddleware


from app.routers import pages, auth, players, apis

from app.core.database import engine
from app.db.base import Base


# Tabloları oluşturur (şimdilik)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Scout Platform")

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET")
)

# Template klasörü
templates = Jinja2Templates(directory="app/templates")

# Static dosyalar (css, js)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(pages.router)
app.include_router(auth.router)
app.include_router(players.router)
app.include_router(apis.router)






