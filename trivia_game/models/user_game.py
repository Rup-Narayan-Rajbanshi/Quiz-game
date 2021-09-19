from django.db import models
from helpers.models import BaseModel
from django.contrib.auth import get_user_model
User = get_user_model()

from .game import Game

class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_game',)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='user_game',)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.user.username)
