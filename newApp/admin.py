from django.contrib import admin

# Register your models here.
from newApp.models import Reservation, Offer, Gallery


admin.site.register(Reservation)
admin.site.register(Offer)
admin.site.register(Gallery)
