from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as dj_login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from django.contrib.auth.models import AnonymousUser

# Create your views here.
def login(request):
    if isinstance(request.user, AnonymousUser):
        error=''
        if request.method == 'GET':
            form = LoginForm()
            data = {
                'form':form,
                'error':error
            }
            return render(request, 'log/login.html', data)
        elif request.method == 'POST':
            form = LoginForm(request,data=request.POST)
            if form.is_valid():
                username = form.data.get('username')
                password = form.data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    dj_login(request,user)
                    messages.success(request,f'Hi {username.title()}, welcome back!')
                    return redirect('profile')
                    
        messages.error(request,f'Invalid username or password')
        return render(request,'log/login.html',{'form': form})
    else:
        return redirect('profile')

        