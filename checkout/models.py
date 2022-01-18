import uuid
from django.db import models
from django.db.models import Sum
from product.models import Item
from profiles.models import UserProfile

class Order(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    street_address1 = models.CharField(max_length=100)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=32, editable=False)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def update_total(self):
        self.order_total = self.orderitems.aggregate(
            Sum('orderitem_total'))['orderitem_total__sum'] or 0
        self.save()

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='orderitems')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_size = models.CharField(max_length=10)
    quantity = models.IntegerField(default=0)
    orderitem_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=0)

    def __str__(self):
        return f'{self.item.name} / {self.order.order_number}'