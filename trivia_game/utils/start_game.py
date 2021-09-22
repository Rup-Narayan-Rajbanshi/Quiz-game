from trivia_game.models.user_game import UserGame
from trivia_game.models.question import Question
from trivia_game.models.user_answer import UserAnswer
from trivia_game.threads import QuestionThread


def start_game(game):
    question = Question.objects.all().first()
    user_games = UserGame.objects.filter(
        game__is_active=True,
        game__is_housefull=True)
    for user_game in user_games:
        obj, created = UserAnswer.objects.get_or_create(
            user_game=user_game,
            question=question)

    QuestionThread(game).start()


