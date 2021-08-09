from django import forms
from .models import AllQuestion


class Question(forms.Form):
    title = forms.CharField(label = "Title", widget = forms.TextInput(
        attrs = {
            "class":"form-control",
            "id":"title",
        }
    ))
    content = forms.CharField(label = "Content", widget = forms.Textarea(
        attrs = {
            "class":"form-control",
            "id":"content",
        }
    ))