from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput, CharField, EmailField


class RegisterForm(UserCreationForm):
    username = CharField(widget=TextInput(attrs={'placeholder' :'Имя пользователя', "style": 'right:50%; transform: translate(400%, 100%);'
}))
    email = EmailField(label= "Почта",widget=EmailInput(attrs={'placeholder' :'Имя почты', "style": 'right:50%; transform: translate(414%, 100%);'}))
    password1 = CharField(label='Пароль',widget=PasswordInput(attrs={'placeholder' :'Пароль', "style": 'right:50%; transform: translate(408%, 100%);'}))
    password2 = CharField(label='Повторите пароль',widget=PasswordInput(attrs={'placeholder' :'Повторите пароль', "style": 'right:50%; transform: translate(364%, 100%);'}))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1",'password2']

    
    