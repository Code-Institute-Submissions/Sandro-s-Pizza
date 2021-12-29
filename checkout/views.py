from django.shortcuts import render


def checkout(request):
    return render(request, 'checkout/checkout.html')


def checkout_complete(request):
    return render(request, 'checkout/checkout_complete.html')

