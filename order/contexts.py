from django.shortcuts import get_object_or_404
from product.models import Item
import datetime


def contexts(request):
    bag_items = []
    grand_total = 0
    delivery_fee = 2
    grand_total += delivery_fee
    order_time = None
    bag = request.session.get('bag', {})
    for item_id, item_data in bag.items():
        product = get_object_or_404(Item, pk=item_id)
        for size, quantity in item_data['size'].items():
            if size == 'small':
                total = quantity * (product.price - 2)
            elif size == 'large':
                total = quantity * (product.price + 2)
            else:
                total = quantity * product.price
            grand_total += total
            order_time = datetime.datetime.now()
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'size': size,
                'total': total            })
    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
        'order_time': order_time,
        'delivery_fee': delivery_fee,
    }
    return context
