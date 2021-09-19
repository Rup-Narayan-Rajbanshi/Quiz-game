from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from trivia_game.forms import *
from trivia_game.models.game import Game
from trivia_game.models.user_game import UserGame
from trivia_game.models.answer import Answer
from trivia_game.models.score import Score


from django.http import HttpResponse
from django.db.models import Max
from django.contrib.auth.decorators import login_required


@login_required(login_url='/user/login/')
def score(request):
    scores = Score.objects.filter(user_game__user=request.user)

    for score in scores:
        game = score.user_game.game
        game_max_score = Score.objects.filter(user_game__game=game).aggregate(Max('score'))
        if game_max_score['score__max'] == score.score:
            if game.is_active == False:
                score.is_winner = True
                score.save()
            else:
                score.is_winner=False
                score.save()
        else:
            score.is_winner=False
            score.save()


    context = {
        'scores':scores
    }

    return render(request,'game/score.html', context)