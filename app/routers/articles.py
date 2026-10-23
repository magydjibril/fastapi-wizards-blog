from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.models.article import Article
from app.db import DbSession, engine
from sqlalchemy import select
from app.schemas.article import ArticleCreate, ArticlePublic, ArticleUpdate
from fastapi import FastAPI, HTTPException, Request

router = APIRouter(prefix="/api/articles", tags=["articles"])


@router.get("")
def get_articles(db: DbSession) -> list[ArticlePublic]: # type: ignore
    return db.scalars(select(Article).order_by(Article.created_at.asc())).all()


@router.get("/{id}", responses={404: {"description": "Article Introuvable"}})
def get_article(db: DbSession, id: int) -> ArticlePublic:
    if not db.get(Article, id):
        raise HTTPException(status_code=404, detail="Pas d'article")
    return db.get(Article, id)

@router.post("", name="create_article", response_model=ArticlePublic,status_code=201)
def created(data: ArticleCreate, db: DbSession) -> ArticlePublic:
    article = Article(**data.model_dump())
    db.add(article)
    db.commit()
    return article

@router.patch("/{id}")
def update_article(article_id: int, data: ArticleUpdate, db: DbSession):
    article = db.get(Article, article_id) # id = 2 dans la db
    if not article:
        raise HTTPException(status_code=404, detail="Pas d'article")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(article,key,value)
    db.commit()
    return article

@router.delete("/{id}", status_code=204)
def delete_article(article_id: int, db: DbSession):
    article = db.get(Article, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Pas d'article")
    db.delete(article)
    db.commit()