from django.shortcuts import render
from .models import Item


def menu(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'product/menu.html', context)


def item(request, item_id):
    context = {
        'item': Item.objects.get(id=item_id)
    }
    return render(request, 'product/item.html', context)
