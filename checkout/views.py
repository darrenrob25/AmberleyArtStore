from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import PurchaseOrderForm 
from products.models import Product

def checkout(request):
    basket = request.session.get('basket', {})
    
    if not basket:
        messages.error(request, "Your shopping basket is currently empty.")
        return redirect(reverse('products'))

    purchase_order_form = PurchaseOrderForm()

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

    # Debugging: print the public key and client secret
    stripe_public_key = 'pk_test_51Q47FiAlhoSxpqB0wbimyXRU09hMuoUWQdrHrVgsFNgRC19rpAopTnKVZWjsmkanqoiMB4CIFY55S15ZMwDy4oIN00hgGlqbdw'
    client_secret = 'test client secret'  # Replace with actual client secret when available
    print("Stripe Public Key:", stripe_public_key)
    print("Client Secret:", client_secret)

    context = {
        'purchase_order_form': purchase_order_form,
        'basket_items': basket_items,
        'product_count': product_count,
        'subtotal': subtotal,
        'shipping': shipping,
        'total_amount': total_amount,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret
    }

    return render(request, 'checkout/checkout.html', context)