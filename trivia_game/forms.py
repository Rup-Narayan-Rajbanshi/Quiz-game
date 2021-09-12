from django import forms
from trivia_game.models.question import Question
from trivia_game.models.answer import Answer
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class AddQuestionForm(forms.ModelForm):
	# confirm_password=forms.CharField(label='Confirm Password')
    
	class Meta:
		model = Question
		fields = [
			'name','order',
			]

	# def clean(self,*args,**kwargs):
		# password = self.cleaned_data.get('password')
		# confirm_password = self.cleaned_data.get('confirm_password')
		# username=self.cleaned_data.get('username')
		# email=self.cleaned_data.get('email')
		# already_registered_user= User.objects.filter(username=username).exists()
		# already_registered_email= User.objects.filter(email=email).exists()
		
		# if password != confirm_password:
		# 	raise forms.ValidationError('Password must match')
		# if already_registered_email == True:
		# 	raise forms.ValidationError('Email already registered, Please register with differenet email')
		# if already_registered_user == True :
		# 	raise forms.ValidationError('User already registered with this username. Please try with another username')
		# code.interact(local = dict(globals(), **locals()))
        # pass

class AddAnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = [
            'text', 'is_correct',
            ]
