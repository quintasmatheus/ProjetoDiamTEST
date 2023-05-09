from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index


app_name = 'MyApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('reset/', views.reset, name='reset'),
    path('aboutUs/', views.about_view, name='aboutUs'),
    path('information/', views.information_view, name='information'),
    path('anunciar/', views.anunciar_view, name='anunciar'),
]
