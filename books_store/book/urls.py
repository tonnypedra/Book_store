from django.urls import path
from . import views

urlpatterns =[
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('contuct', views.contuct, name='contuct'),
    path('registration', views.regisration, name='registration'),
]
