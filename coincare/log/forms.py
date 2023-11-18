from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput, CharField, EmailField

class LoginForm(AuthenticationForm):
    username = CharField(label= '' ,widget=TextInput(attrs={'placeholder':'Username'}))
    password = CharField(label= '' ,widget=PasswordInput(attrs={'placeholder':'Password'}))