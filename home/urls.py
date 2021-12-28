from django.urls import path
from .views import index, contact, message_sent

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('message_sent/', message_sent, name='message_sent'),
]