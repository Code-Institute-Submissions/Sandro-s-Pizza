from django.urls import path
from .views import order, add_item, plus_item, minus_item, delete_item

urlpatterns = [
    path('', order, name='order'),
    path('add_item/<item_id>', add_item, name='add_item'),
    path('plus_item/<item_id>/<size>', plus_item, name='plus_item'),
    path('minus_item/<item_id>/<size>', minus_item, name='minus_item'),
    path('delete_item/<item_id>/<size>', delete_item, name='delete_item'),
]
