import threading
# from .models import *
# from faker import Faker
# fake = Faker()

import time
import random

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

from trivia_game.models.question import Question
from trivia_game.models.answer import Answer
from trivia_game.forms import *

class QuestionThread(threading.Thread):
    
    def __init__(self):
        # self.total = total
        threading.Thread.__init__(self)
    
    def run(self):
        questions = Question.objects.all()
        form=SubmitAnswerForm()
        
        try:
            for question in questions:
                time.sleep(1)
                answer = Answer.objects.filter(question=question)
                channel_layer = get_channel_layer()
                question = question.name
                data = { "question":question, 'a':answer[0].text, 'b':answer[1].text, 'c':answer[2].text, 'd':answer[3].text}
                async_to_sync(channel_layer.group_send)(
                    'new_consumer_group',{
                    'type':'ask_question',
                    'value':json.dumps(data)
                    }
                )
                time.sleep(10)
               
        except Exception as e:
            print(e)