from django.db import models
from helpers.models import BaseModel
from .question import Question


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
        