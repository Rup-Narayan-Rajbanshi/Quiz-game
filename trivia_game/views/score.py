from django.shortcuts import render
from trivia_game.models.score import Score

from django.db.models import Max
from django.contrib.auth.decorators import login_required


@login_required(login_url='/user/login/')
def score(request):
    """
        get the score of the user.
    """
    scores = Score.objects.select_related('user_game').filter(user_game__user=request.user)

    for score in scores:
        game = score.user_game.game
        game_max_score = Score.objects.select_related('user_game').filter(user_game__game=game).aggregate(Max('score'))
        if game_max_score['score__max'] == score.score:
            if not game.is_active:
                score.update(is_winner=True)
            else:
                score.update(is_winner=False)
        else:
            score.update(is_winner=False)
    context = {
        'scores': scores
    }

    return render(request, 'game/score.html', context)