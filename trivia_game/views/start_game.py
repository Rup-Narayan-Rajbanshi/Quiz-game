from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from trivia_game.forms import *
from trivia_game.models.game import Game
from trivia_game.models.user_game import UserGame
from trivia_game.models.answer import Answer
# from .models import *
from django.http import HttpResponse

def start_game(request):
    question = Question.objects.all().first()
    user_games = UserGame.objects.filter(game__is_active=True)
    for user_game in user_games:
        obj, created = UserAnswer.objects.get_or_create(user_game=user_game, question=question)
    
    # user_question = UserAnswer.objects.filter(user_game=user_game).first()
    return render(request,'game/start_game.html')