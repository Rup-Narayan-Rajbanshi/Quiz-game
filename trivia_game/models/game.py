from django.db import models
from helpers.models import BaseModel

class Game(BaseModel):
    questions_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['created_at',]

    def __str__(self):
        return self.questions_count