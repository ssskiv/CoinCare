from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('register/', include('reg.urls')),
    path('login/', include('log.urls')),
    path('profile/',include('account.urls')),
    path('investing/', include('investing.urls')),
]