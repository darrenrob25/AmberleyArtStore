from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import PurchaseOrderForm
from .models import PurchaseOrder, OrderItem
from products.models import Product
from basket.contexts import basket_contents
import stripe

def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        
        if not basket:
            messages.error(request, "Your shopping basket is currently empty.")
            return redirect(reverse('products'))

        form_data = {
            'customer_name': request.POST['customer_name'],
            'customer_email': request.POST['customer_email'],
            'contact_number': request.POST['contact_number'],
            'delivery_country': request.POST['delivery_country'],
            'postal_code': request.POST['postal_code'],
            'city': request.POST['city'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST.get('address_line2', ''),
            'state': request.POST['state'],
        }
        
        purchase_order_form = PurchaseOrderForm(form_data)
        
        if purchase_order_form.is_valid():
            purchase_order = purchase_order_form.save()
            for product_id, quantity in basket.items():
                try:
                    product = Product.objects.get(id=product_id)
                    order_item = OrderItem(order=purchase_order, product=product, quantity=quantity)
                    order_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't found in our database. "
                        "Please call us for assistance!"))
                    purchase_order.delete()
                    return redirect(reverse('products'))

            del request.session['basket']
            messages.success(request, f'Order successfully processed! Your order number is {purchase_order.id}. A confirmation email will be sent to {purchase_order.customer_email}.')
            return redirect(reverse('checkout_success', args=[purchase_order.id]))

        messages.error(request, 'There was an error with your form. Please double-check your information.')

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your shopping basket is currently empty.")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total_amount = current_basket['total_amount']
    stripe_total = round(total_amount * 100)

    try:
        intent = stripe.PaymentIntent.create(amount=stripe_total, currency=settings.STRIPE_CURRENCY)
        client_secret = intent['client_secret']
    except stripe.error.StripeError as e:
        messages.error(request, f"Stripe error occurred: {e.user_message}")
        return redirect(reverse('products'))
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {str(e)}")
        return redirect(reverse('products'))

    purchase_order_form = PurchaseOrderForm()

    context = {
        'purchase_order_form': purchase_order_form,
        'basket_items': current_basket['basket_items'],
        'product_count': current_basket['item_count'],
        'subtotal': current_basket['total_amount'],
        'shipping': current_basket['delivery_cost'],
        'total_amount': current_basket['grand_total'],
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }

    return render(request, 'checkout/checkout.html', context)

def checkout_success(request, order_number):
    order = get_object_or_404(PurchaseOrder, id=order_number)
    messages.success(request, f'Order successfully processed! Your order number is {order_number}. A confirmation email will be sent to {order.customer_email}.')

    if 'basket' in request.session:
        del request.session['basket']

    context = {'order': order}

    return render(request, 'checkout/checkout_success.html', context)