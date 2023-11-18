from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser

from .models import Transaction
from .forms import TransactionForm

def index(request):
    user= request.user
    if not isinstance(user, AnonymousUser):
        transactions = Transaction.objects.filter(uid=user.id)
        return render(request, 'account/index.html', {'user':user, 'list':transactions})
    else:
        return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')

'''def get_user_transactions(request):
    data = Transaction.objects.'''
def add_transaction(request):
    error=''

    if request.method == 'POST':

        request.POST = request.POST.copy()
        request.POST['uid']=request.user.id
        form = TransactionForm(data=request.POST)
        '''obj = form.save(commit=False)
        obj.uid=request.user.id
        form = obj'''
        error+=str( form['uid'])
        
        #form.Meta.model.uid=request.user.id
        
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            error+=str(form.errors)
            error+='НЕВЕРНО'#TODO


    
    data = {
            'form':TransactionForm,
            'error':error,
        }
    return render(request,'account/add_transaction.html', data)