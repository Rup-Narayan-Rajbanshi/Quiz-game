from django.db import models
from helpers.models import BaseModel
from django.contrib.auth import get_user_model
User = get_user_model()

from .game import Game

class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_game',)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='user_game',)
    is_active = models.BooleanField(default=True)
    correct_answers = models.IntegerField(default=0)
    # completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)


# # Create your models here.
# class UserGame(BaseModel):
#     user = models.ForeignKey(User,
# 							on_delete=models.CASCADE,
# 							related_name='user_game',
# 							related_query_name='user_games',
# 							null=True,
# 							)
#     game = models.ForeignKey(Game,
#                         on_delete=models.CASCADE,
#                         related_name='user_game',
#                         related_query_name='user_games',
#                         null=True,
#                         )

#     class Meta:
#         ordering = ["-id"]
