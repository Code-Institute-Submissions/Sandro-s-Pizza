from django.urls import path
from .views import menu, item

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('item/<item_id>', item, name='item'),
]
