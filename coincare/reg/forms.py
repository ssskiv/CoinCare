from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput, CharField, EmailField


class RegisterForm(UserCreationForm):
    username = CharField(widget=TextInput(attrs={'placeholder' :'Username'}))
    email = EmailField(widget=EmailInput(attrs={'placeholder' :'Email'}))
    password1 = CharField(label='Password',widget=PasswordInput(attrs={'placeholder' :'Password'}))
    password2 = CharField(label='Password confirmation',widget=PasswordInput(attrs={'placeholder' :'Password confirmation'}))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1",'password2']

    
    