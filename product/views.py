from django.shortcuts import render, redirect
from .models import Item, Review


def menu(request):
    context = {
        'items': Item.objects.all(),
        'show_bag': True
    }
    return render(request, 'product/menu.html', context)


def item(request, item_id):
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
    return redirect('item', item_id)


def delete_review(request, item_id, review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
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
        return redirect('item', item_id)
    context = {
        'review': review,
    }
    return render(request, 'product/edit_review.html', context)