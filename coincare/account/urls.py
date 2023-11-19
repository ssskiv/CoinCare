from django.contrib import admin
from django.urls import path, include

from . import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('',views.index, name = 'profile'),
    path('logout',views.logout_view, name = 'logout'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('add',views.add_transaction, name='add'),
]
