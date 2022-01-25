from django.shortcuts import render, redirect


def order(request):
    """Renders order page"""
    return render(request, 'order/order.html')


def add_item(request, item_id):
    """Adds item to the bag session variable"""
    size = request.POST['size']
    quantity = int(request.POST['quantity'])
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        if size in bag[item_id]['size'].keys():
            bag[item_id]['size'][size] += quantity
        else:
            bag[item_id]['size'][size] = quantity
    else:
        bag[item_id] = {'size': {size: quantity}}
    request.session['bag'] = bag
    return redirect('menu')


def plus_item(request, item_id, size):
    """Increases quantity of selected item in the bag"""
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        if size in bag[item_id]['size'].keys():
            bag[item_id]['size'][size] += 1
    request.session['bag'] = bag
    return redirect('order')


def minus_item(request, item_id, size):
    """Decreases quantity of selected item in the bag"""
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        if size in bag[item_id]['size'].keys():
            if bag[item_id]['size'][size] > 1:
                bag[item_id]['size'][size] -= 1
            else:
                bag[item_id]['size'][size] = 1
    request.session['bag'] = bag
    return redirect('order')


def delete_item(request, item_id, size):
    """Deletes the item from the bag"""
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        if size in bag[item_id]['size'].keys():
            del bag[item_id]['size'][size]
    # Empty the cart object
    if len(bag[item_id]['size'].keys()) == 0:
        del bag[item_id]
    request.session['bag'] = bag
    return redirect('order')
