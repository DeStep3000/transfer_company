from django.urls import path
from .views import home, book_transfer, contact

urlpatterns = [
    path('', home, name='home'),
    path('book-transfer/', book_transfer, name='book_transfer'),
    path('contact/', contact, name='contact'),
]
