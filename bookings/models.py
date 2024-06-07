from django.conf import settings
from django.db import models


class Vehicle(models.Model):
    type_choices = [
        ('car', 'Car'),
        ('minivan', 'Minivan'),
        ('bus', 'Bus'),
    ]
    type = models.CharField(max_length=20, choices=type_choices)
    license_plate = models.CharField(max_length=10)
    capacity = models.IntegerField()
    description = models.TextField()


class Driver(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    license_number = models.CharField(max_length=20)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
