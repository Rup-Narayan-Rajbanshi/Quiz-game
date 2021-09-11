from django.db import models
from helpers.models import BaseModel
from .game import Game

class Question(BaseModel):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name