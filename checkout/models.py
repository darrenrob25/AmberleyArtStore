import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product
from django_countries.fields import CountryField
from profiles.models import UserProfile

class PurchaseOrder(models.Model):
    order_id = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    customer_email = models.EmailField(max_length=254, null=False, blank=False)
    contact_number = models.CharField(max_length=20, null=False, blank=False)
    delivery_country = CountryField(blank_label='Country *', null=False, blank=False)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    address_line1 = models.CharField(max_length=80, null=False, blank=False)
    address_line2 = models.CharField(max_length=80, null=True, blank=True)
    state = models.CharField(max_length=80, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _create_unique_order_id(self):
        """
        Create a unique order ID using UUID.
        """
        return uuid.uuid4().hex.upper()

    def recalculate_totals(self):
        """
        Recalculate the total amount whenever a line item is added,
        including shipping costs.
        """
        self.subtotal = self.line_items.aggregate(Sum('line_item_total'))['line_item_total__sum'] or 0
        if self.subtotal < settings.FREE_DELIVERY_THRESHOLD:
            self.shipping_cost = self.subtotal * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.shipping_cost = 0
        self.total_amount = self.subtotal + self.shipping_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override save method to generate an order ID if not already set.
        """
        if not self.order_id:
            self.order_id = self._create_unique_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id


class OrderItem(models.Model):
    order = models.ForeignKey(PurchaseOrder, null=False, blank=False, on_delete=models.CASCADE, related_name='line_items')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override save method to calculate line item total
        and update the order's totals.
        """
        self.line_item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Product SKU {self.product.sku} in order {self.order.order_id}'