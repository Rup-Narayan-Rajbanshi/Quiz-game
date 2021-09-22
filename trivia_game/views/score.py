from django.shortcuts import render
from trivia_game.models.score import Score

from django.db.models import Max
from django.contrib.auth.decorators import login_required


@login_required(login_url='/user/login/')
def score(request):
    scores = Score.objects.select_related('user_game').filter(user_game__user=request.user)

    for score in scores:
        game = score.user_game.game
        game_max_score = Score.objects.select_related('user_game').filter(user_game__game=game).aggregate(Max('score'))
        if game_max_score['score__max'] == score.score:
            if not game.is_active:
                score.is_winner = True
                score.save()
            else:
                score.is_winner = False
                score.save()
        else:
            score.is_winner = False
            score.save()
    context = {
        'scores': scores
    }

    return render(request, 'game/score.html', context)