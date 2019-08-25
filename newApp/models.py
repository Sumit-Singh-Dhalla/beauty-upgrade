from django.db import models
from django.utils import timezone
# Create your models here.


class Reservation(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    description = models.TextField()

    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " " + self.phone


class Offer(models.Model):
    name = models.CharField(max_length=150)
    coupon = models.CharField(max_length=30)
    validity = models.DateField(default=timezone.now().date())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " - " + self.coupon
