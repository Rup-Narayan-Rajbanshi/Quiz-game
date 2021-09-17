from django.db import models
from helpers.models import BaseModel
# from django.contrib.auth import get_user_model
from trivia_game.models.user_game import UserGame

# User = get_user_model()

class Score(BaseModel):
    user_game = models.ForeignKey(UserGame, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        return str(self.score)

    @staticmethod
    def calculate_score(score_obj, marks=None):
        return score_obj.score + marks