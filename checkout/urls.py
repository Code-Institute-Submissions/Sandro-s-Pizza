from django.urls import path
from .views import checkout, checkout_complete
from .webhooks import webhook

urlpatterns = [
    path('', checkout, name='checkout'),
    path('checkout_complete/<order_number>', checkout_complete, name='checkout_complete'),
    path('wh/', webhook, name='webhook'),
]
