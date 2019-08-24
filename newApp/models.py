from django.db import models

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