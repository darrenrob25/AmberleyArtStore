from decimal import Decimal
from django.conf import settings

def basket_contents(request):
    """
    Retrieve the current basket details for the session.
    """

    basket_items = []
    total_amount = 0
    item_count = 0

    # Calculate delivery costs based on threshold
    if total_amount < settings.FREE_DELIVERY_THRESHOLD:
        delivery_cost = total_amount * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        amount_needed_for_free_delivery = settings.FREE_DELIVERY_THRESHOLD - total_amount
    else:
        delivery_cost = 0
        amount_needed_for_free_delivery = 0
    
    grand_total = total_amount + delivery_cost
    
    context = {
        'basket_items': basket_items,
        'total_amount': total_amount,
        'item_count': item_count,
        'delivery_cost': delivery_cost,
        'amount_needed_for_free_delivery': amount_needed_for_free_delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context