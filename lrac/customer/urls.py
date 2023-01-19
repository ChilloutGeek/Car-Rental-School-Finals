from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('test2/', views.test2, name='customer')
]