from django.shortcuts import render


def menu(request):
    return render(request, 'product/menu.html')


def item(request):
    return render(request, 'product/item.html')
