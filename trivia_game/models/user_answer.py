from django.db import models
from helpers.models import BaseModel
from .user_game import UserGame
from .question import Question
from .answer import Answer

class UserAnswer(BaseModel):
    user_game = models.ForeignKey(UserGame, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE,null=True,blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_game.user.username)