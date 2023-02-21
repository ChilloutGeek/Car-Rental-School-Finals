from django.shortcuts import render, redirect
from customer.models import CustomerProfile
from .models import Manufacturer,Car,MaintenanceEvent,Rental
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RentalForm

# Create your views here.

class HomeRentalView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        cars = Car.objects.all()
        form = RentalForm()
        currentcustomer = CustomerProfile.objects.get(user=self.request.user)
        return render(request, 'rental/rental.html', {'cars':cars, 'form':form, 'currentcustomer':currentcustomer})

    def post(self, request, pk):

        currentcustomer = CustomerProfile.objects.get(user=self.request.user)

        form = RentalForm(data=request.POST)

        if form.is_valid():
            rentalcreate = form.save(commit=False)
            rentalcreate.Car = Car.objects.get(pk=pk)
            rentalcreate.Renter = currentcustomer
            rentalcreate.save()
        return redirect('rental')






        