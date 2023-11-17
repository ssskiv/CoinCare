from django.shortcuts import render

from django.contrib.auth import authenticate, login

from .forms import LoginForm

# Create your views here.
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'info/index.html', form)

        