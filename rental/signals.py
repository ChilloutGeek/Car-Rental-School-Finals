from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Rental
from customer.models import CustomerProfile


@receiver(post_save, sender=Rental)
def increment_car(sender, instance, created, **kwargs):
    if created:
        car = instance.Car
        car.Stock_Number -= 1
        car.save()

    if instance.FinishedRent:
        profile = CustomerProfile.objects.get(user=instance.Renter.user)
        profile.credit_rating += 5
        profile.save()
    
    else:
        car = instance.Car
        car.Stock_Number += 1
        car.save()

@receiver(post_delete, sender=Rental)
def credit_decrease(sender, instance, **kwargs):

    profile = CustomerProfile.objects.get(user=instance.Renter.user)
    profile.credit_rating -= 5
    profile.save()
