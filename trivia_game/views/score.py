from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from trivia_game.forms import *
from trivia_game.models.game import Game
from trivia_game.models.user_game import UserGame
from trivia_game.models.answer import Answer
from trivia_game.models.score import Score
# from .models import *
from django.http import HttpResponse

def score(request):
    scores = Score.objects.filter(user_game__user=request.user)
    context = {
        'scores':scores
    }

    return render(request,'game/score.html', context)