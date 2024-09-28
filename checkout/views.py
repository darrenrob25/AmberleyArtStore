from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import PurchaseOrderForm

def checkout(request):
    basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, "Your shopping basket is currently empty.")
        return redirect(reverse('products'))

    purchase_order_form = PurchaseOrderForm()

    product_count = sum(item['quantity'] for item in basket.values())
    subtotal = sum(item['price'] * item['quantity'] for item in basket.values())
    shipping = 0
    total_amount = subtotal + shipping

    template = 'checkout/checkout.html'
    context = {
        'purchase_order_form': purchase_order_form,
        'basket_items': basket.values(),
        'product_count': product_count,
        'subtotal': subtotal,
        'shipping': shipping,
        'total_amount': total_amount
    }

    return render(request, template, context)