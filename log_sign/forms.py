from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class Login_form(forms.Form):
	username = forms.CharField(required = True, label = "", widget = forms.TextInput(
		attrs = {
			"placeholder": 'username',
			"class" : "form-control",
			"id":"username",
		}
	))
	password = forms.CharField(required = True, label = "", widget = forms.TextInput(
		attrs = {
			"placeholder": 'password',
			"type":"password",
			"class":"form-control",
			"id":"password",
		}
	))
	def clean_password(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		users = User.objects.all()
		for user in users:
			if str(user.username) == str(username) and check_password(password, user.password):
				return password
		raise forms.ValidationError("Incorrect username or password")


class Signup_form(forms.Form):
	username = forms.CharField(label = "", widget = forms.TextInput(
		attrs = {
			"placeholder": 'username',
			"class" : "form-control",
			"id":'username',
			#'onfocusout':'checking_username()'
		}
	))
	password = forms.CharField(label = "", widget = forms.TextInput(
		attrs = {
			"placeholder": 'password',
			"type":"password",
			"class":"form-control",
			"id":'password'
		}
	))
	confirm_password = forms.CharField(label = "", widget = forms.TextInput(
		attrs = {
			"placeholder": 'confirm password',
			"type":"password",
			"class":"form-control",
			'id':'confirm_password'
		}
	))
	def clean_confirm_password(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if len(password) < 8:
			raise forms.ValidationError('Follow the instructions')
		if password != confirm_password:
			raise forms.ValidationError('Follow the instructions')
		for user in User.objects.all():
			if str(user) == username:
				raise forms.ValidationError('Follow the instructions')
		return password