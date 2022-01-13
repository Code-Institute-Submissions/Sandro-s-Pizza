from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Item, Review
from .forms import ProductForm


def menu(request):
    context = {
        'items': Item.objects.all(),
        'show_bag': True
    }
    return render(request, 'product/menu.html', context)


def item(request, item_id):
    for review in Review.objects.all():
        print(review.user_profile.username)
    context = {
        'item': Item.objects.get(id=item_id),
        'reviews': reversed(Review.objects.all()),
        'show_bag': True
    }
    return render(request, 'product/item.html', context)


def add_review(request, item_id):
    title = request.POST['review__title']
    content = request.POST['review__text']
    current_user = request.user
    current_item = Item.objects.get(id=item_id)
    Review.objects.create(
        user_profile=current_user, item=current_item, title=title, content=content)
    messages.add_message(request, messages.INFO, 'New review added.')
    return redirect('item', item_id)


def delete_review(request, item_id, review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
    messages.add_message(request, messages.INFO, 'Review deleted.')
    return redirect('item', item_id)

def edit_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        print("PRINT: ", review)
        title = request.POST['review__title']
        content = request.POST['review__text']
        review.title = title
        review.content = content
        review.save()
        item_id = review.item.id
        messages.add_message(request, messages.INFO, 'Review updated.')
        return redirect('item', item_id)
    context = {
        'review': review,
    }
    return render(request, 'product/edit_review.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if request.FILES == {}:
            messages.error(request, 'Upload FAILED: Image field is mandatory!')
            return redirect(reverse('add_product'))

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('menu'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    context = {
        'form': form,
    }

    return render(request, 'product/add_product.html', context)