from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Album(models.Model):
    title = fields.TextField()
    artist = fields.TextField()
    year = fields.IntField()
    image_url = fields.TextField()

    def __str__(self):
        return self.title


AlbumSchema = pydantic_model_creator(Album)
