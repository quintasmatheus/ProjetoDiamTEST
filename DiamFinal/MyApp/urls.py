from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import index


app_name = 'MyApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('reset/', views.reset, name='reset'),
    path('aboutUs/', views.about_view, name='aboutUs'),
    path('information/', views.information_view, name='information'),
    path('anunciar/', views.anunciar_view, name='anunciar'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name="register"),
    path('<int:boleia_id>', views.detalhes, name='detalhes'),
    path('user_info/', views.user_info_view, name='user_info'),
]
