from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
# Create your views here.
from .forms import Login_form, Signup_form
from django.urls import reverse
# from .models import Login
from django.contrib.auth.models import User
from django.http import JsonResponse
import json

def login_view(request):
	if 'username' in request.session:
		return HttpResponseRedirect(reverse('home'))
	form = Login_form(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			username = form.cleaned_data["username"]
			request.session['username'] = username
			return HttpResponseRedirect(reverse('home'))
	context = {
		"form":form,
		"error":form.errors.as_json(),
		"logged_in_username":None
	}
	return render(request, "log_sign/login.html", context)

def sign_up_view(request):
	if 'username' in request.session:
		return HttpResponseRedirect(reverse('home'))
	form = Signup_form(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			User.objects.create_user(username = username, password = password)
			request.session['username'] = username
			return  HttpResponseRedirect(reverse('home'))
	else:
		if 'username' in request.GET:
			trying_username = request.GET['username']
			for val in User.objects.all():
				if str(val) == trying_username:
					return JsonResponse({"error":"Username already taken"})
			return JsonResponse({"error":""})
	context = {
		"form":form,
		"error":form.errors.as_json(),
		"logged_in_username":None
	}
	return render(request, "log_sign/sign_up.html", context)

def logout_view(request):
	if 'username' not in request.session:
		return HttpResponseRedirect(reverse('home'))
	if request.method == 'POST':
		del request.session['username']
		return HttpResponseRedirect(reverse('home'))
	logged_in_username = request.session['username']
	context = {
		"logged_in_username":logged_in_username
	}
	return render(request, 'log_sign/logout.html', context)