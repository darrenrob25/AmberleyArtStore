from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem

@receiver(post_save, sender=OrderItem)
def update_purchase_order_total_on_item_save(sender, instance, created, **kwargs):
    """
    Recalculate the purchase order total when an order item is created or updated.
    """
    instance.order.recalculate_totals()

@receiver(post_delete, sender=OrderItem)
def update_purchase_order_total_on_item_delete(sender, instance, **kwargs):
    """
    Recalculate the purchase order total when an order item is deleted.
    """
    instance.order.recalculate_totals()