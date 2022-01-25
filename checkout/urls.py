from django.urls import path
from .views import checkout, checkout_complete, cache_checkout_data
from .webhooks import webhook

urlpatterns = [
    path('', checkout, name='checkout'),
    path(
        'checkout_complete/<order_number>',
        checkout_complete,
        name='checkout_complete'),
    path(
        'cache_checkout_data/',
        cache_checkout_data,
        name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
