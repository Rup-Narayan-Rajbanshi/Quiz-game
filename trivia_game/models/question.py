from django.db import models
from helpers.models import BaseModel


class Question(BaseModel):
    name = models.CharField(max_length=1000)
    order = models.IntegerField(default=0)
    marks = models.IntegerField(default=1)

    def __str__(self):
        return self.name
