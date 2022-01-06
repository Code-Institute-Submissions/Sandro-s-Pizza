from django.urls import path
from .views import menu, item, add_review

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('item/<item_id>', item, name='item'),
    path('add_review/<item_id>', add_review, name='add_review'),
]
