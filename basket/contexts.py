from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):
    """
    Retrieve the current basket details for the session.
    """

    basket_items = []
    total_amount = 0
    item_count = 0
    basket=request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total_amount += quantity * product.price
        item_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

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