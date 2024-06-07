from django.contrib import admin

from .models import Vehicle, Driver, Booking

admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(Booking)
