from django.contrib import admin
from django.urls import path, include
from .views import HomeRentalView,RentalCarView


urlpatterns = [
    path('home/', HomeRentalView.as_view(), name="rental"),
    path('rentacar/<str:pk>', RentalCarView.as_view(), name="rentacar")
]