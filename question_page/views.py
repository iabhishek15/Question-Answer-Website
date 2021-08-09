from django.shortcuts import render, redirect, HttpResponseRedirect, Http404
from pages.forms import Question
from pages.models import AllQuestion, Comments
from datetime import date
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def question_view(request, id):
	question = None
	try:
		question = AllQuestion.objects.get(id = id)
	except ObjectDoesNotExist:
		raise Http404
	logged_in_username = None
	different_user = None
	if 'username' in request.session:
		logged_in_username = request.session["username"]
		if request.is_ajax:
			if 'vote' in request.GET:
				upvote_or_downvote = request.GET.get('vote')
				different_user = vote_change(request, id, upvote_or_downvote)
			if 'delete' in request.GET:
				#deleting the POST
				question.delete()
				return HttpResponseRedirect(reverse('home'))
		if request.method == 'POST':
			username = User.objects.get(username = logged_in_username)
			if 'add_comment' in request.POST:
				#add new comment in the database
				#date_time = datet	ime.datetime.now()
				Comments.objects.create(question = question, username = username, content = request.POST.get("content"), date_time = date.today())
			if 'add_reply' in request.POST:
				#we still need parent and replied to
				parent_id = request.POST.get('parent_id')
				comment_object = Comments.objects.get(id = parent_id) 
				replied = comment_object.username
				parent = comment_object.parent
				if parent is None:
					parent = comment_object
				Comments.objects.create(question = question, username = username,parent = parent, replied_to = replied, content = request.POST.get("content"), date_time = date.today())
		if 'delete_comment' in request.GET:
			comment = Comments.objects.get(id = request.GET.get('delete_comment'))
			comment.delete()
			return HttpResponseRedirect(reverse('question_view', kwargs={"id":id}))
	logged_in = False
	if str(question.username) == logged_in_username:
		logged_in = True
	replies = []
	comments = Comments.objects.filter(question = question, parent = None).order_by('id')
	for comment in comments:
		replies.append(Comments.objects.filter(parent = comment))
	#print(replies)
	context = {
		'question': question,
		'different_user': different_user,
		'logged_in_username':logged_in_username,
		'comments':comments,
		'replies':replies
	}
	return render(request, "question_page/question.html", context)


def vote_change(request, id, upvote_or_downvote):
	question = AllQuestion.objects.get(id = id)
	print(upvote_or_downvote)
	logged_username = request.session["username"]
	user = User.objects.get(username = logged_username)
	if str(question.username) == str(logged_username):
		return "You cannot vote for you own blog"
	if upvote_or_downvote == "upvote":
		if user in question.upvote.all():
			question.upvote.remove(user)
		else:
			question.upvote.add(user)	
			if user in question.downvote.all():
				question.downvote.remove(user)
		return None
	if upvote_or_downvote == "downvote":
		print('downvote is made')
		if user in question.downvote.all():
			question.downvote.remove(user)
		else:
			question.downvote.add(user)
			if user in question.upvote.all():
				question.upvote.remove(user)
		return None
	return None


def testing_view(request):
	if request.method == 'GET' and request.is_ajax:
		title = request.GET.get('title', None)
	a = {
		"name":'abhishek singh',
	}
	context = {
		"data": json.dumps(a),
	}
	return render(request, "question_page/testing.html", context)