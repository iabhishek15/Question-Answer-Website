from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class AllQuestion(models.Model):
	#username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	username = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length = 300)
	content = models.TextField()
	upvote = models.IntegerField(default=0)
	downvote = models.IntegerField(default=0)
	upvote = models.ManyToManyField(User, blank = True, related_name = 'question_upvote')
	downvote = models.ManyToManyField(User, blank = True, related_name = 'question_downvote')
	date = models.CharField(max_length = 100)
	comments_count = models.IntegerField(default = 0)

	def change_comments_count(self):
		print(self)

class Comments(models.Model):
	question = models.ForeignKey(AllQuestion, on_delete = models.CASCADE)
	username = models.ForeignKey(User, on_delete = models.CASCADE, related_name="user")
	parent = models.ForeignKey('self', on_delete = models.CASCADE, blank = True, null = True,related_name="reply_parent")
	# replied_to = models.ForeignKey('self', on_delete = models.CASCADE, blank = True, null = True,related_name="replied_comment")
	replied_to = models.ForeignKey(User, on_delete = models.CASCADE, related_name ="replied_user", null = True, blank = True) 
	content = models.TextField(default = "Defualt is added since cannot think of anything")
	#date_time = models.DateTimeField()
	date_time = models.CharField(max_length = 50)
	upvote = models.ManyToManyField(User, blank = True, related_name = 'comment_upvote')
	downvote = models.ManyToManyField(User, blank = True, related_name = 'comment_downvote')
	reply_comment_count = models.IntegerField(default = 0)
	
	def change_count_comment_reply(self):
		print(self)

# class Comment_reply(models.Model):
# 	parent = models.ForeignKey(Comments, on_delete = models.CASCADE)
# 	replied_to = models.ForeignKey('self', on_delete = models.CASCADE)
# 	user = models.ForeignKey(User, on_delete = models.CASCADE)
# 	content = models.TextField(default="default is added")
# 	date_time = models.CharField(max_length = 50)
# 	upvote = models.ManyToManyField(User, blank = True, related_name = 'comment_upvote')
# 	downvote = models.ManyToManyField(User, blank = True, related_name = 'comment_downvote')

# class UpVote(models.Model):
# 	username = models.CharField(max_length = 100)
	
# 	def __str__(self):
# 		return self.username

# class DownVote(models.Model):
# 	username = models.CharField(max_length = 100)

# 	def __str__(self):
# 		return self.username