from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import BookingForm
from .models import Driver


def home(request):
    return render(request, 'home.html')


@login_required
def book_transfer(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.price = form.calculate_price()

            # Пример логики выбора водителя
            vehicle = booking.vehicle
            driver = Driver.objects.filter(vehicle=vehicle).first()
            booking.driver = driver
            booking.end_time = booking.start_time  # Нужно улучшить логику

            booking.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'book_transfer.html', {'form': form})


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
