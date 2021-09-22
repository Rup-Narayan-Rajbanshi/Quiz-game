
from django.urls import path
from trivia_game.views.join_game import join_game
from trivia_game.views.score import score

app_name = 'trivia_game'

urlpatterns = [
    path('join/', join_game, name='join-game'),
    path('score/', score, name='score'),
]