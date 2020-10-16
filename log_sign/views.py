from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
# Create your views here.
from .forms import Login_form, Signup_form
from django.urls import reverse
# from .models import Login
from django.contrib.auth.models import User


def login_view(request):
	form = Login_form(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			username = form.cleaned_data["username"]
			request.session['username'] = username
			return HttpResponseRedirect("../")
	context = {
		"form":form
	}
	return render(request, "log_sign/login.html", context)

def sign_up_view(request):
	form = Signup_form()
	if request.method == "POST":
		form = Signup_form(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			#Login.objects.create(username = username, password = password)
			User.objects.create_user(username = username, password = password)
			request.session['username'] = username
			return  HttpResponseRedirect("../")
		form = Signup_form()
	context = {
		"form":form
	}
	return render(request, "log_sign/sign_up.html", context)

def logout_view(request):
	if request.method == 'POST':
		del request.session['username']
		return HttpResponseRedirect(reverse('home'))
	logged_in = request.session['username']
	context = {
		"logged_in":logged_in
	}
	return render(request, 'log_sign/logout.html', context)