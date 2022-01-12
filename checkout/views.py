from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderItem
from product.models import Item
from order.contexts import contexts
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'city': request.POST['city'],
        }
        form = OrderForm(form_data)
        if form.is_valid():
            order = form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Item.objects.get(id=item_id)
                    for size, quantity in item_data['size'].items():

                        if size == 'small':
                            orderitem_total = (product.price - 2) * quantity
                        elif size == 'large':
                            orderitem_total = (product.price + 2) * quantity
                        else:
                            orderitem_total = product.price * quantity

                        order_item = OrderItem(
                            order=order,
                            item=product,
                            quantity=quantity,
                            item_size=size,
                            orderitem_total=orderitem_total
                        )                     
                        order_item.save()
                except Item.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in \
                        our database. Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('menu'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_complete', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "Your bag is empty at the moment!")
            return redirect(reverse('menu'))

        current_bag = contexts(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)


def checkout_complete(request, order_number):
    """
    Handle complete checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if 'bag' in request.session:
        del request.session['bag']

    context = {
        'order': order,
    }
    return render(request, 'checkout/checkout_complete.html', context)
