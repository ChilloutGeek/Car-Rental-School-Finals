from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rental


@receiver(post_save, sender=Rental)
def increment_car(sender, instance, created, **kwargs):
    if created:
        car = instance.Car
        car.Stock_Number -= 1
        car.save()
    else:
        car = instance.Car
        car.Stock_Number += 1
        car.save()