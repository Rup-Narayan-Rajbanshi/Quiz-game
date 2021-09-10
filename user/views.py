from django.contrib.auth import ( authenticate , get_user_model , login, logout )
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, Http404
import code
# from custom_decorators.decorator import *

def register_view(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		user=form.save(commit=False)
		password=form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		return HttpResponseRedirect(reverse('home'))

	context={
		'form':form,
	}

	return render(request,'user/register.html',context=context)


# Create your views here.
def login_view(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user=authenticate(username=username, password=password)
		login(request,user)

		return HttpResponseRedirect(reverse('index'))


	context = {'form':form}
	return render(request,'user/login.html',context=context)

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('user:login'))


def user_update_view(request,id):
	instance=get_object_or_404(User,id=id)
	form = EditUserForm(request.POST or None,instance=instance)
	if form.is_valid():
		user=form.save(commit=False)
		user.save()

		return HttpResponseRedirect(reverse('index'))
	else:
		form=EditUserForm(request.POST or None,instance=instance)

	context={
		'form':form,
	}

	return render(request,'user/register.html',context=context)
