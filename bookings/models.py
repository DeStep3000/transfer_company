from django.conf import settings
from django.db import models


class Vehicle(models.Model):
    type_choices = [
        ('car', 'Легковой автомобиль'),
        ('van', 'Фургон'),
        ('truck', 'Грузовик'),
    ]
    type = models.CharField(max_length=20, choices=type_choices)
    license_plate = models.CharField(max_length=10)
    capacity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.get_type_display()} ({self.license_plate})"


class Driver(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    license_number = models.CharField(max_length=20)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


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

    def __str__(self):
        return f"Booking from {self.start_location} to {self.end_location} at {self.start_time}"
