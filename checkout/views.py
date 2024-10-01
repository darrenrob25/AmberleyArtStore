from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import PurchaseOrderForm 
from products.models import Product
from basket.contexts import basket_contents
import stripe

def checkout(request):
    # Set the Stripe API key from the settings
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Retrieve the shopping basket from the session
    basket = request.session.get('basket', {})
    
    # If the basket is empty, show an error message and redirect
    if not basket:
        messages.error(request, "Your shopping basket is currently empty.")
        return redirect(reverse('products'))

    # Get the current basket contents and calculate the total amount
    current_basket = basket_contents(request)
    total_amount = current_basket['total_amount']
    stripe_total = round(total_amount * 100)  # Stripe expects the amount in cents

    # Create a PaymentIntent and handle potential errors
    try:
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
        client_secret = intent['client_secret']  # Get the client secret from the created intent
    except stripe.error.StripeError as e:
        messages.error(request, f"Stripe error occurred: {e.user_message}")
        return redirect(reverse('products'))
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {str(e)}")
        return redirect(reverse('products'))

    # Prepare the purchase order form
    purchase_order_form = PurchaseOrderForm()

    # Retrieve basket items
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

    # Calculate additional totals
    product_count = sum(item['quantity'] for item in basket_items)
    subtotal = sum(item['product'].price * item['quantity'] for item in basket_items)
    shipping = 0  # Update as needed based on your logic
    total_amount = subtotal + shipping

    # Prepare context for rendering the template
    context = {
        'purchase_order_form': purchase_order_form,
        'basket_items': basket_items,
        'product_count': product_count,
        'subtotal': subtotal,
        'shipping': shipping,
        'total_amount': total_amount,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': client_secret
    }

    return render(request, 'checkout/checkout.html', context)