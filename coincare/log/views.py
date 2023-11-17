from django.shortcuts import render

from django.contrib.auth import authenticate, login

from .forms import LoginForm

# Create your views here.
def login(request):
    error=''
    if request.method == 'GET':
        form = LoginForm()
        data = {
            'form':form,
            'error':error
        }
        return render(request, 'log/login.html', data)
    if request.method == 'POST':
        

        