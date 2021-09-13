from django.shortcuts import redirect,render
from trivia_game.forms import *
from trivia_game.models.question import Question
from trivia_game.models.user_game import UserGame
from trivia_game.models.answer import Answer
from django.http import HttpResponse

def question(request):
    # user = request.user
    # score = 0
    # user_game = UserGame.objects.filter(user=user).first()
    # # question = Question.objects.get(id=question_id)
    # user_question_answer_obj = UserAnswer.objects.filter(user_game=user_game,answer=None).first()

    # if not user_question_answer_obj == None: 
    #     user_question_answer_obj = UserAnswer.objects.filter(user_game=user_game,answer=None).first()

    #     question = user_question_answer_obj.question
    #     answers = Answer.objects.filter(question=question)
    #     right_answer = answers.objects.filter(is_correct=True)
    #     next_question = Question.objects.filter(id__gt=question.id).order_by('id').first()

    #     form=SubmitAnswerForm()
    #     if(request.method=='POST'):
    #         form=SubmitAnswerForm(request.POST)
    #         if(form.is_valid()):
    #             if form.data['answer_option']=='a':
    #                 user_question_answer_obj.update(answer=answers[0])
    #             elif form.data['answer_option']=='b':
    #                 user_question_answer_obj.update(answer=answers[1])
    #             elif form.data['answer_option']=='c':
    #                 user_question_answer_obj.update(answer=answers[2])
    #             else:
    #                 user_question_answer_obj.update(answer=answers[3])
            
    #             if user_question_answer_obj.answer == right_answer:
    #                 score = score + 1
    #             else:
    #                 user_game.update(is_active=False)
                       
    #             try :
    #                 user_question_answer_obj, created = UserAnswer.objects.get_or_create(user_game=user_game, question=next_question)
    #             except:
    #                 return redirect('home')

    #             return redirect('trivia_game:question')

    #     context={
    #         'question':question,
    #         'a':answers[0],
    #         'b':answers[1],
    #         'c':answers[2],
    #         'd':answers[3],
    #         'form':form,
    #         'score':score
    #         }
    # else:
    #     context={}
    #     return render(request,'game/question.html',context)

    context={}  

    return render(request,'game/question.html',context)
