from typing import Annotated, Literal


from fastapi import APIRouter, Path, Query, Request
from fastapi import status
from app.schemas.products import ProductCreate

router = APIRouter(tags=["exercices"])


@router.get("/products/new")
def newProduct() -> str:
    return "Nouveau produit"

@router.get("/products/{id}")
def product(id: Annotated[int, Path(ge=1)]) -> dict[str, str]:
    return {"message": f"Produit n°{id}"}

@router.post("/products", status_code=status.HTTP_201_CREATED)
def prices(produit: ProductCreate) -> ProductCreate:
    return produit



@router.get("/search")
def search(q: Annotated[str, Query(min_length=3)], limit: Annotated[int, Query(le=50)] = 10) -> dict[str, str]:
    return {"message": f"Recherche : {q}, limite : {limit}"}


@router.get("/categories/{name}")
def country(name: str , country: Literal["fr","en"] | None = None) ->  dict[str, str] :
    return {"message":f"Nom : {name} ,Pays: {country or 'Pays non précisé'}"}

@router.get("/sizes/{size}")
def taille(size: Literal["small", "medium", "large"] | None = None) -> dict[str, str] :
    return {"message": f"Taille : {size or 'Taille non défini'}"}

@router.get("/sessions/{uuid}")
def session(uuid: Annotated[str, Path(regex="[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}")]):
    return {"message": f"Produit {uuid}"}


@router.get("/debug/{value}")
def valeur(value: str, request: Request):
    return {"message": f"valeur = {value}, la méthode = {request.method}, url = {request.url}, en tete = {request.headers}"}

