from decimal import Decimal

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class ProductCreate(BaseModel):
    name: str
    price: Decimal = Field(gt=0, decimal_places=2)


