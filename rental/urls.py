from django.contrib import admin
from django.urls import path, include
from .views import HomeRentalView, UpdateRentalView, RentaCarView


urlpatterns = [
    path('home/', HomeRentalView.as_view(), name="rental"),
    path('rentacar/<str:pk>/', RentaCarView.as_view(), name="rentacar"),
    path('editrent/<str:pk>/', UpdateRentalView.as_view(), name="update")
]