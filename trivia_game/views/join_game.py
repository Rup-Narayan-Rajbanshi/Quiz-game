from trivia_game.forms import SubmitAnswerForm
from trivia_game.models.game import Game
from trivia_game.models.user_game import UserGame
from trivia_game.models.answer import Answer
from trivia_game.models.user_answer import UserAnswer
from trivia_game.models.question import Question
from trivia_game.models.score import Score
from trivia_game.utils.start_game import start_game
from trivia_game.threads import AnswerChoiceThread

from django.contrib import messages
from django.db.models import Count
from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url='/user/login/')
def join_game(request):
    user = request.user
    game_exist = Game.objects.filter(is_active=True, is_housefull=False).exists()
    user_active_in_existing_game = UserGame.objects.filter(user=user, is_active=True).exists()

    if user_active_in_existing_game:
        user_game = UserGame.objects.select_related('game', 'user').filter(user=user, is_active=True).first()
        game = user_game.game

    elif game_exist:
        game = Game.objects.filter(is_active=True, is_housefull=False).first()
        user_game, created = UserGame.objects.get_or_create(user=user, game=game, is_active=True)

        user_game_count = UserGame.objects.filter(game=game).count()
        if user_game_count == game.no_of_participants:
            game.update(is_housefull=True)
            start_game(game)

    else:
        game = Game.objects.create()
        UserGame.objects.filter(user=user, is_active=True).update(is_active=False)
        user_game = UserGame.objects.create(user=user, game=game)

    user_question_answer_obj = UserAnswer.objects.filter(user_game=user_game, answer=None).first()

    form = SubmitAnswerForm()
    if user_question_answer_obj:
        question = user_question_answer_obj.question
        answers = Answer.objects.filter(question=question)
        right_answer = answers.filter(is_correct=True).first()
        next_question = Question.objects.filter(id__gt=question.id).order_by('id').first()

        form = SubmitAnswerForm()
        if(request.method == 'POST'):
            form = SubmitAnswerForm(request.POST)
            if(form.is_valid()):
                if form.data['answer_option'] == 'a':
                    user_question_answer_obj.update(answer=answers[0])
                elif form.data['answer_option'] == 'b':
                    user_question_answer_obj.update(answer=answers[1])
                elif form.data['answer_option'] == 'c':
                    user_question_answer_obj.update(answer=answers[2])
                else:
                    user_question_answer_obj.update(answer=answers[3])

                # update which user choosed each answer
                AnswerChoiceThread(user, question).start()

                # Update Score on selecting right answer
                if user_question_answer_obj.answer == right_answer:
                    score_obj, created = Score.objects.get_or_create(user_game=user_game)
                    score_obj.score = score_obj.score + question.marks
                    score_obj.save()

                # Update Score on selecting wrong answer
                else:
                    score_obj, created = Score.objects.get_or_create(user_game=user_game)
                    score_obj.score = score_obj.score
                    score_obj.save()

                    # make user game deactive on selecting wrong answer
                    user_game.is_active = False
                    user_game.save()
                    messages.success(request, 'Wrong Answer. You are Terminated')

                    return redirect('trivia_game:score')
   
                try:
                    user_question_answer_obj, created = UserAnswer.objects.get_or_create(user_game=user_game, question=next_question)            
                except UserAnswer.DoesNotExist:
                    messages.success(request, 'Congratulation You are a Winner')
                    score_obj.is_winner = True
                    score_obj.save()
                    UserGame.objects.filter(game=game).update(is_active=False)
                    game = game.update(is_active=False)
                    return redirect('trivia_game:score')

                return redirect('trivia_game:join-game')

        context = {
            'form': form,
            'question': question,
            'user_answers': Answer.objects.filter(question=question).annotate(ans=Count('useranswer', Q(useranswer__user_game__game=game))),
            'user': request.user.username,
            'question_id': question.id if question else Question.objects.all().first().id,
        }
    else:
        context = {
                'form': form,
                'question_id': Question.objects.all().first().id,
                }
        return render(request, 'game/question.html', context)

    return render(request, 'game/question.html', context)
