from django.db import models
from helpers.models import BaseModel
from .user_game import UserGame
from .question import Question
from .answer import Answer
# from .score import Score


class UserAnswer(BaseModel):
    user_game = models.ForeignKey(UserGame, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_game.user.id)

    def get_answer_is_correct(self):
        if self.answer:
            return self.answer == self.get_right_answer

    # @property
    # def get_right_answer(self):
    #     answers = Answer.objects.filter(question=self.question)
    #     right_answer = answers.filter(is_correct=True).first()
    #     return right_answer

    # @staticmethod
    # def set_score(user_game, marks=None):
    #     score_obj, created = Score.objects.get_or_create(user_game=user_game)
    #     score_obj.score = score_obj.calculate_score(score_obj, question.marks)
    #     score_obj.save()
