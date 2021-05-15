from fastapi import APIRouter

from app.api import crud
from app.models.pydantic import AlbumSchema

router = APIRouter(prefix="/albums", tags=["albums"])


@router.get("/{title}", response_model=AlbumSchema)
async def read_album(title: str) -> AlbumSchema:
    album = await crud.get(title)
    return album


@router.get("/", response_model=list[AlbumSchema])
async def read_all_albums() -> list[AlbumSchema]:
    return await crud.get_all()


@router.post("/", response_model=AlbumSchema, status_code=201)
async def create_album(payload: AlbumSchema) -> AlbumSchema:
    album = await crud.post(payload=payload)
    return album
