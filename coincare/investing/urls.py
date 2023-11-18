from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index, name = 'investing'),#127.0.0.1:8000/investing/a/
]