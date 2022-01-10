from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_total', 'date', 'order_number', 'original_bag', 'stripe_pid')

class OrderItemAdmin(admin.ModelAdmin):
    readonly_fields = ('orderitem_total',)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)