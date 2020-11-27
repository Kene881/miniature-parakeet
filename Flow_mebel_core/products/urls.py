from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all, name = 'products'),
    path('register', views.get_all, name = 'register'),
]