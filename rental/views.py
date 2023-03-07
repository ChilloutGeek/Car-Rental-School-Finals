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
        
        #get car data 
        cars = Car.objects.all()
        form = RentalForm()
        currentcustomer = CustomerProfile.objects.get(user=self.request.user)
        
        #search functionality
        search_text = request.GET.get('search_text', None)
        if search_text:
            cars = Car.objects.get(Model__contains=search_text)

        return render(request, 'rental/rental.html', {'cars':cars, 'form':form, 'currentcustomer':currentcustomer})

    def post(self, request, pk):

        #POST interaction for renting a car
        currentcustomer = CustomerProfile.objects.get(user=self.request.user)

        form = RentalForm(data=request.POST)

        #Saving form data when renting 
        if form.is_valid():
            rentalcreate = form.save(commit=False)
            rentalcreate.Car = Car.objects.get(pk=pk)
            rentalcreate.Renter = currentcustomer
            rentalcreate.save()
        return redirect('rental')

class RentaCarView(LoginRequiredMixin, View):
    
    login_url = 'login'


    def get(self, request, pk):
        
        current_car = Car.objects.get(pk=pk)
        current_user = CustomerProfile.objects.get(user=request.user)
        customer_rents = Rental.objects.filter(Renter=current_user)

        instance = Rental.objects.create(Car=current_car, Renter=current_user)


        form = RentalForm(instance=instance)
        return render(request, 'rental/rentacar.html', {'form':form, 'customer_rents':customer_rents, 'current_user':current_user, 'car':current_car})


    def post(self, request, pk):

        current_car = Car.objects.get(pk=pk)
        form = RentalForm(data=request.POST)

        #Saving form data when renting 
        if form.is_valid():
            rentalcreate = form.save(commit=False)
            rentalcreate.Car = current_car
            rentalcreate.Renter = current_user
            rentalcreate.save()
        return redirect('rental')

        

class UpdateRentalView(LoginRequiredMixin, View):
        
        login_url = 'login'

        def get(self, request, pk):
            rental = Rental.objects.get(pk=pk)

            form = RentalForm(instance=rental)

            currentcustomer = CustomerProfile.objects.get(user=self.request.user)

            return render(request, 'rental/editrent.html', {'rental':rental, 'form':form, 'currentcustomer':currentcustomer})
        
        def post(self, request, pk):
            
            rental = Rental.objects.get(pk=pk)
            currentcustomer = CustomerProfile.objects.get(user=self.request.user)
            form = RentalForm(request.POST, instance=rental)

            if form.is_valid():
                rentedform = form.save(commit=False)
                rentedform.Car = Car.objects.get(pk=pk)
                rentedform.Renter = currentcustomer
                rentedform.save()
            return redirect('rental')




        