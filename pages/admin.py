from django.contrib import admin

# Register your models here.
from .models import AllQuestion, Comments

admin.site.register(AllQuestion)
admin.site.register(Comments)
# admin.site.register(UpVote)
# admin.site.register(DownVote)