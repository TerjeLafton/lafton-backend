from typing import Union

from app.models.pydantic import AlbumSchema
from app.models.tortoise import Album


async def get(title: str) -> Union[dict, None]:
    album = await Album.filter(title__icontains=title).first().values()
    if album:
        return album[0]
    return None


async def get_all() -> list:
    albums = await Album.all().values()
    return albums


async def post(payload: AlbumSchema) -> AlbumSchema:
    album = Album(**payload.dict())
    await album.save()
    return album
