from django.contrib import admin
from django.urls import path, include
from .views import HomeRentalView, FinishRentView, RentaCarView


urlpatterns = [
    path('home/', HomeRentalView.as_view(), name="rental"),
    path('rentacar/<str:pk>/', RentaCarView.as_view(), name="rentacar"),
    path('finishrent/<str:pk>/', FinishRentView.as_view(), name="finishrent")
]