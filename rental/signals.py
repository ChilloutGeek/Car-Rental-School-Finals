from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Rental
from customer.models import CustomerProfile
from django.utils import timezone
import pytz

ph_tz = pytz.timezone('Asia/Manila')
now = timezone.now().astimezone(ph_tz)

@receiver(post_save, sender=Rental)
def increment_car(sender, instance, created, **kwargs):
    if created:
        car = instance.Car
        car.Stock_Number -= 1
        car.save()

    if instance.FinishedRent and instance.ReturnDate < now :
        profile = CustomerProfile.objects.get(user=instance.Renter.user)
        profile.credit_rating -= 5
        profile.save()

        car = instance.Car
        car.Stock_Number += 1
        car.save()

    else:

        profile = CustomerProfile.objects.get(user=instance.Renter.user)
        profile.credit_rating += 5
        profile.save()

        car = instance.Car
        car.Stock_Number += 1
        car.save()

@receiver(post_delete, sender=Rental)
def credit_decrease(sender, instance, **kwargs):

    profile = CustomerProfile.objects.get(user=instance.Renter.user)
    profile.credit_rating -= 5
    profile.save()
