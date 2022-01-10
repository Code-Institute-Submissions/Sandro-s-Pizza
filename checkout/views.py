from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty at the moment!")
        return redirect(reverse('menu'))
    form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'checkout/checkout.html', context)


def checkout_complete(request):
    return render(request, 'checkout/checkout_complete.html')
