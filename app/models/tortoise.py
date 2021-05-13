from tortoise import fields, models


class Album(models.Model):
    title = fields.TextField()
    artist = fields.TextField()
    year = fields.IntField()
    url = fields.TextField()

    def __str__(self):
        return self.title
