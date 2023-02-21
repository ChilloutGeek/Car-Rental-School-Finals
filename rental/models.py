from django.db import models
from django.conf import settings
from customer.models import CustomerProfile
User = settings.AUTH_USER_MODEL
# Create your models here.

class Manufacturer(models.Model):
    Country = models.CharField(max_length=200)
    Sales_Name = models.CharField(max_length=200)
    Sales_RepNumber = models.IntegerField()

class Car(models.Model):
    Renter = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)
    Model = models.CharField(max_length=200)
    Class = models.IntegerField()

    def __str__(self):
        return str(self.Model)

class MaintenanceEvent(models.Model):
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    Date = models.DateTimeField()
    Procedure = models.CharField(max_length=500)
    Mileage = models.IntegerField()
    Repair_Time = models.IntegerField()

class Rental(models.Model):
    Car = models.OneToOneField(Car, on_delete=models.CASCADE)
    ReturnDate = models.DateTimeField()
    RentalDate = models.DateTimeField()
    TotalCost = models.IntegerField()



