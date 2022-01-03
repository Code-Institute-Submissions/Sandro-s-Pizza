from django.shortcuts import render
from .models import Item


def menu(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'product/menu.html', context)


def item(request):
    return render(request, 'product/item.html')
