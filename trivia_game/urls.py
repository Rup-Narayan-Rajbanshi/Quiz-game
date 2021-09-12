
from django.urls import path
from trivia_game.views.questions import *
# from apis.views import *

app_name = 'trivia_game'

urlpatterns = [
    path('add_question/', addQuestion, name='add-question'),
    # path('logout/', logout_view, name='logout'),
    # path('register/',register_view, name='register'),
    # path('update/<int:id>/',user_update_view,name='update'),
]