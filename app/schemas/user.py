from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr
from app.db import DbSession


class User(BaseModel):
  email: Optional[EmailStr]
  is_admin: Optional[bool] = False
  hashed_password: str




class UserCreate(User):
  model_config = ConfigDict(from_attributes=True)


class UserPublic(User):
  id : int


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    username: str | None = None
