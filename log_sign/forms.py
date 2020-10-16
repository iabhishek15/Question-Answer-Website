from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class Login_form(forms.Form):
	username = forms.CharField(label = "", widget = forms.TextInput(
		attrs = {
			"placeholder": 'username',
			"class" : "form-control",
		}
	))
	password = forms.CharField(label = "", widget = forms.TextInput(
		attrs = {
			"placeholder": 'password',
			"type":"password",
			"class":"form-control"
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
		}
	))
	password = forms.CharField(label = "", widget = forms.TextInput(
		attrs = {
			"placeholder": 'password',
			"type":"password",
			"class":"form-control"
		}
	))
	confirm_password = forms.CharField(label = "", widget = forms.TextInput(
		attrs = {
			"placeholder": 'confirm password',
			"type":"password",
			"class":"form-control"
		}
	))
	# def clean_username(self, *args, **kwargs):
	# 	username = self.cleaned_data.get("username")
	# 	query_set = Login.objects.all()
	# 	for val in query_set:
	# 		if val.username == username:
	# 			raise forms.ValidationError("username already exits")
	# 	return username

	# def clean_password(self, *args, **kwargs):
	# 	password = self.cleaned_data.get("password")
	# 	if len(password) < 8:
	# 		raise forms.ValidationError("password is too short")
	# 	return password

	# def clean_confirm_password(self, *args, **kwargs):
	# 	password = self.cleaned_data.get("password")
	# 	confirm_password = self.cleaned_data.get('confirm_password')
	# 	if password != confirm_password:
	# 		raise forms.ValidationError("passwords do not match")
	# 	return confirm_password
