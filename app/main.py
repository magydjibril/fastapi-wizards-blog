from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.schemas.article import ArticleBase, ArticleCreate, ArticlePublic
from app.models.article import Article
from app.routers import exercices, articles, auth
from app.db import DbSession, engine
from sqlalchemy import select


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    engine.dispose()



app = FastAPI(title="Blog des Wizards", lifespan=lifespan)

app.include_router(exercices.router)
app.include_router(articles.router)
app.include_router(auth.router)


templates = Jinja2Templates(directory="app/templates")
@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> dict[str, str]:
    return templates.TemplateResponse(request, "home.html", {"titre": "Le blog de djibril", "articles": get_articles()})

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}



