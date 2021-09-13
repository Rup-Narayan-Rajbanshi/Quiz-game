from django.db import models
from helpers.models import BaseModel

class Game(BaseModel):
    questions_count = models.IntegerField(default=0)
    no_of_participants = models.IntegerField(default=10)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at',]

    def __str__(self):
        return str(self.id)