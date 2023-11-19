from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser

from .models import Transaction
from .forms import TransactionForm
from .data_handle import DataHandle


def index(request):
    user = request.user

    if not isinstance(user, AnonymousUser):

        transactions = Transaction.objects.filter(uid=user.id)
        dh=DataHandle(request,transactions)
        dh.generate_plots()
        return render(request, 'account/index.html', {'user': user, 'list': transactions, 'data':dh, 'table':dh.html, 'barplot':dh.barplot})

    else:
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')


'''def get_user_transactions(request):
    data = Transaction.objects.'''


def add_transaction(request):
    error = ''

    if request.method == 'POST':

        request.POST = request.POST.copy()
        request.POST['uid'] = request.user.id
        form = TransactionForm(data=request.POST)
        '''obj = form.save(commit=False)
        obj.uid=request.user.id
        form = obj'''
        error += str(form['uid'])

        # form.Meta.model.uid=request.user.id

        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            error += str(form.errors)
            error += 'НЕВЕРНО'  # TODO

    data = {
        'form': TransactionForm,
        'error': error,
    }
    return render(request, 'account/add_transaction.html', data)
def all_transactions(request):
        user = request.user
        transactions = Transaction.objects.filter(uid=user.id)
        dh=DataHandle(request,transactions)
        return render(request, 'account/table.html',{'table':dh.full_html})