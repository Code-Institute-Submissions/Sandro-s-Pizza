from django.urls import path
from .views import checkout, checkout_complete

urlpatterns = [
    path('', checkout, name='checkout'),
    path('checkout_complete/', checkout_complete, name='checkout_complete'),
]
