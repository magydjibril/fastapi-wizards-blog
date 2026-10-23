from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ArticleBase(BaseModel):
    titre : str
    contenu : str


class ArticleCreate(ArticleBase):
    model_config = ConfigDict(from_attributes=True)

class ArticlePublic(ArticleBase):
    id: int
    created_at : datetime

class ArticleUpdate(BaseModel):
    titre: str | None = None
    contenu: str | None = None
