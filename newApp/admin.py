from django.contrib import admin

# Register your models here.
from newApp.models import Reservation, Offer


admin.site.register(Reservation)
admin.site.register(Offer)
