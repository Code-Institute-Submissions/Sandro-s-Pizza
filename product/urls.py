from django.urls import path
from .views import menu, item, add_review, delete_review, edit_review, add_product, edit_product, delete_product

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('item/<item_id>', item, name='item'),
    path('add_review/<item_id>', add_review, name='add_review'),
    path(
        'delete_review/<item_id>/<review_id>',
        delete_review,
        name='delete_review'),
    path('edit_review/<review_id>', edit_review, name='edit_review'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<item_id>/', edit_product, name='edit_product'),
    path('delete/<item_id>/', delete_product, name='delete_product'),
]
