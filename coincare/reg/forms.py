from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1",'password2']

        '''widgets = {
            'username':TextInput(attrs={
                'class':'form-control'
            }),
            'email':EmailInput(attrs={
                'class':'form-control'
            }),
            'password1':PasswordInput(attrs={
                'class':'form-control'
            }),
            'password2':PasswordInput(attrs={
                'class':'form-control'
            })
        }'''
