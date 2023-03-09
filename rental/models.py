from django.db import models
from django.conf import settings
from customer.models import CustomerProfile
User = settings.AUTH_USER_MODEL
# Create your models here.

class Manufacturer(models.Model):
    ManufacturerName = models.CharField(max_length=200, null=True)
    Country = models.CharField(max_length=200, null=True)
    Sales_Name = models.CharField(max_length=200, null=True)
    Sales_RepNumber = models.IntegerField(null=True)

    def __str__(self):
        return str(self.ManufacturerName)


class MaintenanceEvent(models.Model):
    RepairNumber = models.IntegerField(null=True) 
    Date = models.DateTimeField(null=True)
    Procedure = models.CharField(max_length=500)
    Mileage = models.IntegerField(null=True)
    Repair_Time = models.IntegerField(null=True)

    def __str__(self):
        return str(self.Procedure)

class Car(models.Model):
    CarPicture = models.ImageField(upload_to='cars/', blank=True)
    Manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    Model = models.CharField(max_length=200,null=True)
    Class = models.IntegerField(null=True)
    Maintenance = models.ManyToManyField(MaintenanceEvent)
    Stock_Number = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.Model)  

class Rental(models.Model):
    Car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    Renter = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)
    ReturnDate = models.DateTimeField(null=True)
    RentalDate = models.DateTimeField(auto_now_add=True, null=True)
    TotalCost = models.IntegerField(null=True)
    FinishedRent = models.BooleanField(default=0)

    def __str__(self):
        return str(self.Renter)


