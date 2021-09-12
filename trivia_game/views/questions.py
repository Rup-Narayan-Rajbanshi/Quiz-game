from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from trivia_game.forms import *
# from .models import *
from django.http import HttpResponse

def addQuestion(request):    
    if request.user.is_superuser:
        form=AddQuestionForm()
        if(request.method=='POST'):
            form=AddQuestionForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('home')
        context={'form':form}
        return render(request,'game/addQuestion.html',context)
    else: 
        return redirect('home')