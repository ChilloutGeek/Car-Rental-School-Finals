from django.contrib import admin
from django.urls import path, include
from .views import HomeRentalView


urlpatterns = [
    path('home/', HomeRentalView.as_view(), name="rental")
   
]