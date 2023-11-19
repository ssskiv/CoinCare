from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index, name = 'investing'),
    path('add', views.add_trade, name='add_trade'),
    path('all', views.all_trades, name='all_trades'),
]