from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput, CharField, EmailField


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    username = CharField(widget=TextInput(attrs={'placeholder' :'Username'}))
    email = EmailField(widget=EmailInput(attrs={'placeholder' :'Email'}))
    password1 = CharField(label='Password',widget=PasswordInput(attrs={'placeholder' :'Password'}))
    password2 = CharField(label='Password confirmation',widget=PasswordInput(attrs={'placeholder' :'Password confirmation'}))

    widgets = {
        'username':TextInput(attrs={
            'class':'form-control'
        }),
        'email':EmailInput(attrs={
            'placeholder' :'Email', 
            'class':'form-control'
        }),
        'password1':PasswordInput(attrs={
            'class':'form-control'
        }),
        'password2':PasswordInput(attrs={
            'class':'form-control'
        })
    }
    
    class Meta:
        model = User
        fields = ["username", "email", "password1",'password2']

    
    