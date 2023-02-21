from django.contrib import admin
from django.urls import path, include
from .views import signup_acc, login_acc, logout_acc, car_list

urlpatterns = [
    path('signup/', signup_acc, name='signup'),
    path('login/', login_acc, name='login'),
    path('logout/', logout_acc, name='logout'),
     path('profile/', car_list, name='car')
]