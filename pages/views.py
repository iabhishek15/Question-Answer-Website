from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import AllQuestion
# Create your views here.
from .forms import Question
from datetime import date
import json
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.urls import reverse

def home_page_view(request):
	questions = AllQuestion.objects.all()
	paginator = Paginator(questions,10);
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	logged_in_username = None
	if 'username' in request.session:
		logged_in_username = request.session['username']
	context = {
		"questions": page_obj,
		'logged_in_username':logged_in_username
	}
	return render(request,'pages/home.html', context)


def add_question_view(request):
	form = Question()
	try:
		logged_in_username = request.session['username']
	except KeyError:
		return HttpResponseRedirect(reverse('signup'))
	if request.method == 'POST':
		new_form = Question(request.POST)
		if new_form.is_valid():
			title = new_form.cleaned_data["title"]
			content = new_form.cleaned_data["content"]	
			user = User.objects.get(username = request.session['username'])
			AllQuestion.objects.create(username = user, title = title, content = content, date = date.today())
			curr_id = AllQuestion.objects.all().order_by("-id")[0].id
			return HttpResponseRedirect(reverse("question_view", kwargs={"id":curr_id}))
	context = {
		"form":form,
		'logged_in_username':logged_in_username,
	}
	return render(request, "pages/add_question.html", context)


def question_edit_view(request, id):
	question = AllQuestion.objects.get(id = id)
	logged_in_username = request.session['username']
	if request.method == 'POST':
		title = request.POST["title"]
		content = request.POST["content"]
		question.title = title
		question.content = content
		question.save()
		return HttpResponseRedirect(reverse('question_view',kwargs = {'id':id}))
	context = {
		"question": question,
		'logged_in_username':logged_in_username
	}
	return render(request, 'pages/edit_question.html',context)
