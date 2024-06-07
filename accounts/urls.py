from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import register, verify_phone, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('verify-phone/', verify_phone, name='verify_phone'),
    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
