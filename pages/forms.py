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


# class SignUp_form(forms.ModelForm):
#     username = forms.CharField(label = "", widget = forms.TextInput(
#         attrs = {
#             "placeholder":"username"
#         } 
#     ))
#     name = forms.CharField(label = "", widget = forms.TextInput(
#         attrs = {
#             "placeholder":"name"
#         } 
#     ))
#     email = forms.EmailField(label = "", widget = forms.EmailInput(
#         attrs = {
#             "placeholder":"email"
#         } 
#     ))
#     password = forms.CharField(label = "", widget = forms.TextInput(
#         attrs = {
#             "placeholder":"password"
#         } 
#     ))
#     confirmpassword = forms.CharField(label = "", widget = forms.TextInput(
#         attrs = {
#             "placeholder":"confirm password"
#         } 
#     ))
#     number = forms.CharField(label = "", widget = forms.TextInput(
#         attrs = {
#             "placeholder":"mobile number"
#         } 
#     ))
#     class Meta:
#         model = SignUp
#         fields = [
#             "username",
#             "name",
#             "email",
#             "password",
#             "confirmpassword",
#             "number"
#         ]
#     def clean_username(self, *args, **kwargs):
#         username = self.cleaned_data.get("username")
#         #forms.ValidationError
#         queryall = SignUp.objects.all()
#        # print(queryall)
#         for val in queryall:
#             if val.username == username:
#                 raise forms.ValidationError("username already taken")
#         if len(username) > 20:
#             raise forms.ValidationError("too long user name")
#         return username

#     def clean_email(self, *args, **kwargs):
#         email = self.cleaned_data.get("email")
#         queryall = SignUp.objects.all()
#        # print(queryall)
#         for val in queryall:
#             if val.email == email:
#                 raise forms.ValidationError("email already exits")
#         #print(len(str(email)))
#         # if str(email).endswith("@gmail.com") == False:
#         #     raise forms.ValidationError("invalid email type")
#         return email

#     def clean_password(self, *args, **kwargs):
#         password = self.cleaned_data.get("password")
#         if len(password) < 8:
#             raise forms.ValidationError("password to short")
#         return password

#     def clean_confirmpassword(self, *args, **kwargs):
#         password = self.cleaned_data.get("password")
#         confirmpassword = self.cleaned_data.get("confirmpassword")
#         if password != None:
#             if password != confirmpassword:
#                 raise forms.ValidationError("passwords do not match")
#         return password

#     def clean_number(self, *args, **kwargs):
#         number = self.cleaned_data.get("number")            
#         if len(number) != 10:
#             raise forms.ValidationError("number length is not valid")
#         return number


# class Login_form(forms.Form):
#     username = forms.CharField(label = "", widget = forms.TextInput( 
#         attrs = {
#             "placeholder" : "username",
#         }
#     ))
#     password = forms.CharField(label = "", widget = forms.TextInput( 
#         attrs = {
#             "placeholder" : "password",
#         }
#     ))
#     def clean_password(self, *args, **kwargs):
#         username = self.cleaned_data.get("username")
#         password = self.cleaned_data.get("password")
#         query_all = SignUp.objects.all();
#         for val in query_all:
#             if val.username == username and val.password == password:
#                 return password
#         raise forms.ValidationError("username or password is incorrect")
        
#     