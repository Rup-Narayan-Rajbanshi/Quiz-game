from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from trivia_game.forms import *
from trivia_game.models.game import Game
from trivia_game.models.user_game import UserGame
from trivia_game.models.answer import Answer
from trivia_game.models.user_answer import UserAnswer
from trivia_game.models.score import Score
# from .models import *
from django.http import HttpResponse

def join_game(request):
    user = request.user
    score = 0
    game_exist = Game.objects.filter(is_active=True).exists()
    if game_exist == True:
        print("game_exists")
        game = Game.objects.filter(is_active=True).first()
        user_game, created = UserGame.objects.get_or_create(user=user, game=game, is_active=True)
        print(user_game)
        print(created)
    else:
        print("new game")
        game = Game.objects.create()
        user_game = UserGame.objects.create(user=user, game=game)

    user_question_answer_obj = UserAnswer.objects.filter(user_game=user_game,answer=None).first()
    print(user_question_answer_obj)

    if not user_question_answer_obj == None:
        print("Inside if")
        user_question_answer_obj = UserAnswer.objects.filter(user_game=user_game,answer=None).first()

        question = user_question_answer_obj.question
        answers = Answer.objects.filter(question=question)
        right_answer = answers.filter(is_correct=True).first()
        print(right_answer)
        next_question = Question.objects.filter(id__gt=question.id).order_by('id').first()

        form=SubmitAnswerForm()
        if(request.method=='POST'):
            form=SubmitAnswerForm(request.POST)
            if(form.is_valid()):
                if form.data['answer_option']=='a':
                    user_question_answer_obj.update(answer=answers[0])
                elif form.data['answer_option']=='b':
                    user_question_answer_obj.update(answer=answers[1])
                elif form.data['answer_option']=='c':
                    user_question_answer_obj.update(answer=answers[2])
                else:
                    user_question_answer_obj.update(answer=answers[3])
            

                if user_question_answer_obj.answer == right_answer:
                    print(score)
                    score_obj,created = Score.objects.get_or_create(user_game=user_game)
                    score_obj.score = score_obj.score + 1
                    score_obj.save()
                else:
                    score_obj,created = Score.objects.get_or_create(user_game=user_game)
                    score_obj.score = score_obj.score
                    score_obj.save()
                    user_game.is_active=False
                    user_game.save()
                    return redirect('trivia_game:score')

                       
                try :
                    print("try")
                    user_question_answer_obj, created = UserAnswer.objects.get_or_create(user_game=user_game, question=next_question)
                    print(created)
                    print("user_answer_obj= ",user_question_answer_obj)              
                except:
                    return redirect('trivia-game:score')

                return redirect('trivia_game:join-game')

        context={
            'question':question,
            'a':answers[0],
            'b':answers[1],
            'c':answers[2],
            'd':answers[3],
            'form':form,
            # 'score':score_obj.score if score_obj.score else '0'
            }
    else:
        context={}
        return render(request,'game/question.html',context)
    print("context=",context)

        

    return render(request,'game/question.html',context)
