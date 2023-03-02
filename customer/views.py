from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from customer.models import CustomerProfile
from rental.models import Car, Rental
from .forms import LoginForm, SignUpForm

# Create your views here.

def signup_acc(request):
    
    form = SignUpForm()

    if request.method == 'POST':
        
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request, 'customer/signuppage.html', {'form': form})

def login_acc(request):
    
    form = LoginForm()

    if request.method == "POST":
        
        form = LoginForm(request.POST, request=request)
        
        if form.is_valid():
            
            login(request, form.user)
            
            return redirect("rental")

    return render(request, 'customer/loginpage.html', {'form':form})


def logout_acc(request):
    logout(request)
    return redirect('login')

def profile_page(request,pk):
    
    #get user's car rents
    user = request.user
    profile = CustomerProfile.objects.get(user=user)
    rentals = Rental.objects.filter(Renter=profile)



    return render(request, 'customer/customer.html', {'rentals':rentals})


