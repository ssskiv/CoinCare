from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput, CharField, EmailField


class RegisterForm(UserCreationForm):
    username = CharField(label= "", widget=TextInput(attrs={'placeholder' :'Имя пользователя', "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}))
    email = EmailField(label= "", widget=EmailInput(attrs={'placeholder' :'Электронная почта', "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}))
    password1 = CharField(label= "", widget=PasswordInput(attrs={'placeholder' :'Пароль', "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}))
    password2 = CharField(label= "" ,widget=PasswordInput(attrs={'placeholder' :'Повторите пароль', "style": "border-radius: 6px; border:1px solid; margin-bottom: 2%; box-shadow: inset 0 0 4px rgba(0, 0, 0, 0.2)"}))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1",'password2']

    
    