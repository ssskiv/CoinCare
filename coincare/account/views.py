from django.shortcuts import render, redirect

from django.contrib.auth import logout

def index(request):
    user= request.user
    return render(request, 'account/index.html', {'id':user.id})

def logout_view(request):
    logout(request)
    return redirect('index')