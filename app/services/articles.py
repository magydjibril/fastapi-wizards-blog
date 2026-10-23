from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.models.article import Article
from app.db import DbSession, engine
from sqlalchemy import select
from app.schemas.article import ArticleCreate, ArticlePublic, ArticleUpdate
from fastapi import FastAPI, HTTPException, Request



def get_article_or_404(db: DbSession, article_id: int):
    article = db.get(Article, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Pas d'article")
    return article