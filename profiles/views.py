from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """
    get_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=get_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=get_profile)
    orders = get_profile.orders.all()[::-1]

    context = {
        'form': form,
        'orders': orders
    }

    return render(request, 'profiles/profile.html', context)


@login_required()
def saved_order(request, order_number):
    """Renders specific single order in order history"""
    order = get_object_or_404(Order, order_number=order_number)
    # Check if user is allowed to see the order
    if not str(order.user_profile) == request.user.username:
        messages.error(request, 'Permission denied.')
        return redirect(reverse('index'))
    context = {
        'order': order,
    }
    return render(request, 'profiles/saved_order.html', context)
