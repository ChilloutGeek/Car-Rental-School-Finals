from django.contrib import admin
from django.urls import path, include
from .views import HomeRentalView, FinishRentView, RentaCarView, SearchResultsView, HardDeleteRentalView


urlpatterns = [
    path('home/', HomeRentalView.as_view(), name="rental"),
    path('rentacar/<str:pk>/', RentaCarView.as_view(), name="rentacar"),
    path('finishrent/<str:pk>/', FinishRentView.as_view(), name="finishrent"),
    path('results/', SearchResultsView.as_view(), name="searchresults"),
    path('cancelrent/<str:pk>/', HardDeleteRentalView.as_view(), name="cancelrent")
]