from django.db import models
from helpers.models import BaseModel
from .user_game import UserGame
from .question import Question
from .answer import Answer

class UserAnswer(BaseModel):
    user_game = models.ForeignKey(UserGame, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
            self.question.name