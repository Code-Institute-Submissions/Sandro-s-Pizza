from django.http import HttpResponse
from .models import Order, OrderItem
from product.models import Item
import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                            full_name__iexact=shipping_details.name,
                            email__iexact=billing_details.email,
                            phone_number__iexact=shipping_details.phone,
                            city__iexact=shipping_details.address.city,
                            street_address1__iexact=shipping_details.address.line1,
                            street_address2__iexact=shipping_details.address.line2,
                            order_total=grand_total,
                            original_bag=bag,
                            stripe_pid=pid,
                        )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    original_bag=bag,
                    stripe_pid=pid,
                    )
                for item_id, item_data in json.loads(bag).items():
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)