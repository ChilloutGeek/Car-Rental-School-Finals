from django.contrib import admin
from django.urls import path, include
from .views import signup_acc, login_acc, logout_acc, profile_page, edit_page

urlpatterns = [
    path('signup/', signup_acc, name='signup'),
    path('login/', login_acc, name='login'),
    path('logout/', logout_acc, name='logout'),
    path('profile/<str:pk>/', profile_page, name='profile'),
    path('editprofile/<str:pk>/', edit_page, name='edit')
    
]