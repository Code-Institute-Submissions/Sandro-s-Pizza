from django.shortcuts import render, redirect


def order(request):
    return render(request, 'order/order.html')


def add_item(request, item_id):
    size = request.POST['size']
    quantity = int(request.POST['quantity'])
    url = request.POST['url']
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        if size in bag[item_id]['size'].keys():
            bag[item_id]['size'][size] += quantity
        else:
            bag[item_id]['size'][size] = quantity
    else:
        bag[item_id] = {'size': {size: quantity}}
    request.session['bag'] = bag
    return redirect(url)
