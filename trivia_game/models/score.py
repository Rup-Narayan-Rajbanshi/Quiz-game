from django.db import models
from helpers.models import BaseModel
from trivia_game.models.user_game import UserGame


class Score(BaseModel):
    user_game = models.ForeignKey(UserGame, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    is_winner = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.score)

    @staticmethod
    def calculate_score(score_obj, marks=None):
        return score_obj.score + marks