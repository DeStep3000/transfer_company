from django.urls import path
from .views import register, verify_phone, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('verify-phone/', verify_phone, name='verify_phone'),
    path('profile/', profile, name='profile'),
]
