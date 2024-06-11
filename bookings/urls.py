from django.urls import path
from .views import home, book_transfer, contact, contact_success, transfer_success

urlpatterns = [
    path('', home, name='home'),
    path('book-transfer/', book_transfer, name='book_transfer'),
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
    path('transfer-success/', transfer_success, name='transfer_success'),
]
