from datetime import UTC, datetime, timedelta, timezone


import jwt
from fastapi import APIRouter,FastAPI, Depends, status
from pwdlib import PasswordHash
from app.models.user import User
from app.schemas.user import UserCreate, UserPublic, Token, TokenData
from app.services.user import check_user_or_404
from app.services.user import check_user_or_409
from app.db import DbSession
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from app.config import settings


SECRET_KEY = "5c3afd96f948bb9c6d3faab5ba05b176735af62f87eaa5b66fc5457a62b1a706"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


router = APIRouter(prefix="/auth", tags=["auth"])
password_hash = PasswordHash.recommended()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register", name="register", response_model=UserPublic, status_code=201)
def create_authentification(db: DbSession, data: UserCreate) -> UserPublic :
    check_user_or_409(db, data)
    data.hashed_password = password_hash.hash(data.hashed_password)
    user = User(**data.model_dump())
    db.add(user)
    db.commit()
    return user

@router.post("/token", name="token")
def auth_user(db: DbSession, data: UserCreate) -> Token:
    user= check_user_or_404(db, data)
    if user and password_hash.verify(data.hashed_password, user.hashed_password):
        print("oui")
    return Token(access_token=create_token(user))

def create_token(user: User) -> str:
    exp = datetime.now(UTC) + timedelta(minutes=30)
    return jwt.encode({"sub": str(user.id), "exp": exp}, settings.secret_key)



