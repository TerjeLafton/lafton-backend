from datetime import date
from typing import Optional

from pydantic import BaseModel, HttpUrl


class AlbumSchema(BaseModel):
    title: str
    artist: str
    year: int
    image_url: HttpUrl
