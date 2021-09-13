
from django.urls import path
from trivia_game.views.join_game import join_game
from trivia_game.views.question import question
from trivia_game.views.start_game import start_game
# from apis.views import *

app_name = 'trivia_game'

urlpatterns = [
    # path('add_question/', addQuestion, name='add-question'),
    path('join/', join_game, name='join-game'),
    path('start/', start_game, name='start-game'),
    path('question/', question, name='question'),
    # path('register/',register_view, name='register'),
    # path('update/<int:id>/',user_update_view,name='update'),
]