
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import random
import threading
import time
import json
from django.db.models import Count
from django.db.models import Q

from trivia_game.models.question import Question
from trivia_game.models.answer import Answer
from trivia_game.models.user_game import UserGame
from trivia_game.models.user_answer import UserAnswer
from trivia_game.forms import *



class QuestionThread(threading.Thread):
    
    def __init__(self, game):
        self.game = game
        threading.Thread.__init__(self)
    
    def run(self):
        questions = Question.objects.all()
        form=SubmitAnswerForm()
        
        try:
            for question in questions:
                time.sleep(1)
                answer = Answer.objects.filter(question=question)
                channel_layer = get_channel_layer()
                question_name = question.name
                data = { "question":question_name, 'question_id':str(question.id), 'a':answer[0].text, 'b':answer[1].text, 'c':answer[2].text, 'd':answer[3].text}
                async_to_sync(channel_layer.group_send)(
                    'new_consumer_group',{
                    'type':'ask_question',
                    'value':json.dumps(data)
                    }
                )

                time.sleep(20)
                timeout_useranswers = UserAnswer.objects.values_list('user_game__id', flat = True).filter(user_game__game=self.game,\
                                                                                                        question=question, \
                                                                                                        answer=None)

                user_games = UserGame.objects.filter(id__in=timeout_useranswers).update(is_active=False)
                all_user_games_inactive_exists = UserGame.objects.filter(game=self.game, is_active=False).exists()
                if all_user_games_inactive_exists:
                    game = self.game
                    game.is_active = False
                    game.save()
               
        except Exception as e:
            print(e)

class AnswerChoiceThread(threading.Thread):
    
    def __init__(self, user, question):
        self.user = user
        self.question = question
        threading.Thread.__init__(self)
    
    def run(self):
        game = UserGame.objects.filter(user=self.user).first().game
        print("thread 2 running")
        try:
            user_answers=Answer.objects.filter(question=self.question).annotate(\
                                            ans=Count('useranswer', 
                                            Q(useranswer__user_game__game=game))),

            channel_layer = get_channel_layer()
            question_name = self.question.name
            data2 = {
                    "question_order":self.question.order,
                    'answer_count_a':user_answers[0][0].ans,
                    'answer_count_b':user_answers[0][1].ans,
                    'answer_count_c':user_answers[0][2].ans,
                    'answer_count_d':user_answers[0][3].ans,
                    }
            async_to_sync(channel_layer.group_send)(
                'new_consumer_group',{
                'type':'get_answer_choice',
                'value':json.dumps(data2)
                }
            )
            time.sleep(1)
               
        except Exception as e:
            print(e)