from django.db import models
from helpers.models import BaseModel


class Game(BaseModel):
    no_of_participants = models.IntegerField(default=3)
    is_active = models.BooleanField(default=True)
    is_housefull = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at', ]

    def __str__(self):
        return str(self.id)
