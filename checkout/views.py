from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import PurchaseOrderForm
from products.models import Product  # Ensure this import points to your Product model

def checkout(request):
    basket = request.session.get('basket', {})
    print("Basket:", basket)  # Debugging statement

    if not basket:
        messages.error(request, "Your shopping basket is currently empty.")
        return redirect(reverse('products'))

    purchase_order_form = PurchaseOrderForm()

    # Retrieve products from the database using their IDs
    basket_items = []
    for product_id, quantity in basket.items():
        try:
            product = Product.objects.get(id=product_id)
            basket_items.append({
                'product': product,
                'quantity': quantity
            })
        except Product.DoesNotExist:
            messages.error(request, f"Product with ID {product_id} does not exist.")
            return redirect(reverse('products'))

    product_count = sum(item['quantity'] for item in basket_items)
    subtotal = sum(item['product'].price * item['quantity'] for item in basket_items)
    shipping = 0  # Set your shipping logic here
    total_amount = subtotal + shipping

    template = 'checkout/checkout.html'
    context = {
        'purchase_order_form': purchase_order_form,
        'basket_items': basket_items,
        'product_count': product_count,
        'subtotal': subtotal,
        'shipping': shipping,
        'total_amount': total_amount
    }

    return render(request, template, context)