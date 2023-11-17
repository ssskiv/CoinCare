from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(request):
    error=''
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account')
        else:
            error='НЕВЕРНО'#TODO
    form = RegisterForm()

    data = {
        'form':form,
        'error':error
    }

    return render(request, 'reg/register.html', data)

def index(request):
    return render(request, 'reg/register.html')