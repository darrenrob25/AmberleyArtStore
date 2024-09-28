from django.contrib import admin
from .models import PurchaseOrder, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('line_item_total',)


class PurchaseOrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_id', 'order_date',
                       'shipping_cost', 'subtotal',
                       'total_amount',)

    fields = ('order_id', 'order_date', 'customer_name',
              'customer_email', 'contact_number', 'delivery_country',
              'postal_code', 'city', 'address_line1',
              'address_line2', 'state', 'shipping_cost',
              'subtotal', 'total_amount',)

    list_display = ('order_id', 'order_date', 'customer_name',
                    'subtotal', 'shipping_cost',
                    'total_amount',)

    ordering = ('-order_date',)

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)