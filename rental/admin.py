from django.contrib import admin
from .models import Car, MaintenanceEvent, Rental, Manufacturer

# Register your models here.
admin.site.register(Car)
admin.site.register(MaintenanceEvent)
admin.site.register(Rental)
admin.site.register(Manufacturer)

