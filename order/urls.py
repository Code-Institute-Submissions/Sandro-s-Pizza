from django.urls import path
from .views import order, add_item

urlpatterns = [
    path('', order, name='order'),
    path('add_item/<item_id>', add_item, name='add_item'),
]
