from django.shortcuts import render, redirect
from .forms import TradeForm
from .models import Trade
from django.contrib.auth.models import AnonymousUser
from .trades_handle import TradesHandle
# Create your views here.


def index(request):
    user = request.user

    if not isinstance(user, AnonymousUser):
        transactions = Trade.objects.filter(uid=user.id)
        dh=TradesHandle(request,transactions)
        dh.generate_plots()
        
        return render(request, 'investing/index.html', {'user': user, 'list': transactions, 'data':dh, 'table':dh.html, 'barplot':dh.barplot})

    else:
        return redirect('index')

def add_trade(request):
    error = ''

    if request.method == 'POST':

        request.POST = request.POST.copy()
        request.POST['uid'] = request.user.id

        transactions = Trade.objects.filter(uid=request.user.id)
        dh=TradesHandle(request,transactions)

        request.POST['trade_price']=dh.get_price(request.POST['token'])

        form = TradeForm(data=request.POST)
        '''obj = form.save(commit=False)
        obj.uid=request.user.id
        form = obj'''
        error += str(form['uid'])

        # form.Meta.model.uid=request.user.id

        if form.is_valid():
            form.save()
            return redirect('investing')
        else:
            error += str(form.errors)
            error += 'НЕВЕРНО'  # TODO

    data = {
        'form': TradeForm,
        'error': error,
    }
    return render(request, 'investing/add_trade.html', data)
def all_trades(request):
    user = request.user
    transactions = Trade.objects.filter(uid=user.id)
    dh=TradesHandle(request,transactions)
    return render(request, 'account/table.html',{'table':dh.full_html})