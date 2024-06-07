from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Booking, Vehicle, Driver


def home(request):
    return render(request, 'home.html')


def book_transfer(request):
    if request.method == 'POST':
        start_location = request.POST['start_location']
        end_location = request.POST['end_location']
        start_time = request.POST['start_time']
        user = request.user

        # Пример логики выбора автомобиля и водителя
        vehicle = Vehicle.objects.first()  # Необходимо улучшить логику
        driver = Driver.objects.first()  # Необходимо улучшить логику

        booking = Booking.objects.create(
            user=user,
            driver=driver,
            vehicle=vehicle,
            start_location=start_location,
            end_location=end_location,
            start_time=start_time,
            end_time=start_time,  # Необходимо улучшить логику
            price=100,  # Пример, необходимо улучшить логику
            status='Pending'
        )
        return HttpResponseRedirect('/')

    return render(request, 'book_transfer.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            f'Message from {name}',
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
        )
        return render(request, 'contact_success.html')
    return render(request, 'contact.html')
