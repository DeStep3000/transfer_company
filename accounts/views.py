import random

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from twilio.rest import Client

from bookings.models import Booking
from .forms import CustomUserCreationForm, VerifyPhoneForm
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Деактивируем пользователя до подтверждения номера
            user.save()

            # Отправка SMS с кодом подтверждения
            code = random.randint(100000, 999999)
            request.session['verification_code'] = code
            request.session['phone_number'] = user.phone_number

            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            client.messages.create(
                body=f"Ваш код подтверждения: {code}",
                from_=settings.TWILIO_PHONE_NUMBER,
                to=user.phone_number
            )

            return redirect('verify_phone')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def verify_phone(request):
    if request.method == 'POST':
        form = VerifyPhoneForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            if code == str(request.session['verification_code']):
                phone_number = request.session['phone_number']
                user = CustomUser.objects.get(phone_number=phone_number)
                user.is_phone_verified = True
                user.is_active = True
                user.save()
                login(request, user)
                return redirect('home')
    else:
        form = VerifyPhoneForm()
    return render(request, 'accounts/verify_phone.html', {'form': form})


@login_required
def profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'accounts/profile.html', {'bookings': bookings})
