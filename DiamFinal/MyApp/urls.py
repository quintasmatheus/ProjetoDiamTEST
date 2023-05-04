from django.contrib import admin
from django.urls import path, include
from . import views
from .views import boleias

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.boleias, name='boleias'),
]
