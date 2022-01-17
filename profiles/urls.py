from django.urls import path
from .views import profile, saved_order

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('saved_order/<order_number>', saved_order, name='saved_order'),
]
