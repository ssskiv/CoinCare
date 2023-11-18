from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index, name = 'profile'),
    path('logout',views.logout_view, name = 'logout'),
    path('add',views.add_transaction, name='add'),
]
