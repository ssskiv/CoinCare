from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput, CharField, EmailField

class LoginForm(AuthenticationForm):
    username = CharField(label= '' ,widget=TextInput(attrs={'placeholder':'Имя пользователя', "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}))
    password = CharField(label= '' ,widget=PasswordInput(attrs={'placeholder':'Пароль', "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}))