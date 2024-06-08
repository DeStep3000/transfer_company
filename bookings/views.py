from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import BookingForm
from .forms import ContactForm
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
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'Контактное сообщение от {name}'
            message_body = f'Имя: {name}\nEmail: {email}\nСообщение:\n{message}'

            send_mail(
                subject,
                message_body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
            )
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')
