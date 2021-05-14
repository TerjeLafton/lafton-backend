from datetime import datetime

from pydantic import BaseModel, HttpUrl

class AlbumSchema(BaseModel):
    title: str
    artist: str
    year: datetime.year
    url: HttpUrl
