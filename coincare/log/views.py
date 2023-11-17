from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):
    error=''
    if request.method == 'GET':
        form = AuthenticationForm()
        data = {
            'form':form,
            'error':error
        }
        return render(request, 'log/login.html', data)
    else:
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error='Неправильно введено имя пользователя или пароль'
                
        else:
            error='Неправильно введено имя пользователя или пароль'
    return render(request, 'log/login.html', {'form':form,'error':error})



        