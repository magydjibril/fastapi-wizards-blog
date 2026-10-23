from app.models.article import Article
from app.db import DbSession
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserCreate
from sqlalchemy import select
from pwdlib import PasswordHash





def check_user_or_409(db: DbSession, data: UserCreate):
    user = db.scalar(select(User).where(User.email == data.email))
    if user:
        raise HTTPException(status_code=409, detail="Email déjà existant")
    return user


def check_user_or_404(db: DbSession, data: UserCreate):
    user = db.scalar(select(User).where(User.email == data.email))
    if not user:
        raise HTTPException(status_code=404, detail="Email non existant")
    return user

