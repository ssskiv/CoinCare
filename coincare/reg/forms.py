from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput, CharField, EmailField


class RegisterForm(UserCreationForm):
    username = CharField(label= "", widget=TextInput(attrs={'placeholder' :'Имя пользователя'}))
    email = EmailField(label= "", widget=EmailInput(attrs={'placeholder' :'Электронная почта'}))
    password1 = CharField(label= "", widget=PasswordInput(attrs={'placeholder' :'Пароль'}))
    password2 = CharField(label= "" ,widget=PasswordInput(attrs={'placeholder' :'Повторите пароль'}))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1",'password2']

    
    