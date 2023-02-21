from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

class Manufacturer(models.Model):
    Country = models.CharField(max_length=200)
    Sales_Name = models.CharField(max_length=200)
    Sales_RepNumber = models.IntegerField()

class Car(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Model = models.CharField(max_length=200)
    Class = models.IntegerField()

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



