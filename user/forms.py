from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import Group, Permission
import code

User = get_user_model()


class RegisterForm(forms.ModelForm):
	confirm_password = forms.CharField(label='Confirm Password')
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password',
			'confirm_password',
			]

	def clean(self, *args, **kwargs):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')
		already_registered_user = User.objects.filter(username=username).exists()
		already_registered_email = User.objects.filter(email=email).exists()
		
		if password != confirm_password:
			raise forms.ValidationError('Password must match')
		if already_registered_email == True:
			raise forms.ValidationError('Email already registered, Please register with differenet email')
		if already_registered_user == True :
			raise forms.ValidationError('User already registered with this username. Please try with another username')
		# code.interact(local = dict(globals(), **locals()))


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			if field in ("username"):
				self.fields[field].widget.attrs.update({'placeholder': 'Username'})
			if field in ("password"):
				self.fields[field].widget.attrs.update({'placeholder': 'Password'})
			self.fields[field].label=''

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)

		if not user:
			raise forms.ValidationError('The user doesnot exist')
		if not user.check_password(password):
			raise forms.ValidationError('The password is incorrect')
		if not user.is_active:
			raise forms.ValidationError('The user is not active')


class EditUserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			]

	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')
		
		already_registered_user = User.objects.filter(username = username).exclude(id=self.instance.id).exists()
		
		already_registered_email = User.objects.filter(email = email).exclude(id=self.instance.id).exists()
		
		if already_registered_email == True:
			print(already_registered_email)
			raise forms.ValidationError('Email already registered, Please update with differenet email')
		if already_registered_user == True :
			raise forms.ValidationError('User already registered with this username. Please try with another username')







