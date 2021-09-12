from django.contrib import admin
from trivia_game.models.game import Game
from trivia_game.models.user_game import UserGame
from trivia_game.models.question import Question
from trivia_game.models.answer import Answer
from trivia_game.models.user_answer import UserAnswer

import nested_admin


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4

# class QuestionInline(nested_admin.NestedTabularInline):
#     model = Question
#     inlines = [AnswerInline,]
#     extra = 19

class GameAdmin(nested_admin.NestedModelAdmin):
    inlines = [AnswerInline,]

# class UserAnswerInline(admin.TabularInline):
#     model = UserAnswer


# class UserGameAdmin(admin.ModelAdmin):
#     inlines = [UserAnswerInline,]

admin.site.register(Question, GameAdmin)
# admin.site.register(UserGame, UserGameAdmin)
# admin.site.register(UserAnswer)

