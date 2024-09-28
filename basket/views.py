from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from products.models import Product

def view_basket(request):
    """ A view to view your basket """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add products to basket """
    quantity = int(request.POST.get('quantity', 0))
    redirect_url = request.POST.get('redirect_url', reverse('view_basket'))  # Default to view_basket

    basket = request.session.get('basket', {})
    
    if quantity <= 0:
        messages.error(request, "Invalid quantity. Please enter a valid number.")
        return redirect(redirect_url)

    # Get product name for messages
    try:
        product = Product.objects.get(id=item_id)
    except Product.DoesNotExist:
        messages.error(request, "Product does not exist.")
        return redirect(redirect_url)

    if item_id in basket.keys():
        basket[item_id] += quantity
        messages.success(request, f"Updated quantity of {product.name} in your basket.")
    else:
        basket[item_id] = quantity
        messages.success(request, f"Added {product.name} to your basket.")

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Edit the basket."""
    basket = request.session.get('basket', {})
    
    if item_id not in basket:
        messages.error(request, "Item not found in your basket.")
        return redirect('view_basket')  # Redirect to view basket

    # Get product name for messages
    try:
        product = Product.objects.get(id=item_id)
    except Product.DoesNotExist:
        messages.error(request, "Product does not exist.")
        return redirect('view_basket')  # Redirect to view basket

    try:
        quantity = int(request.POST.get('quantity', 0))

        if quantity > 0:
            basket[item_id] = quantity  # Set the new quantity
            messages.success(request, f"Updated quantity of {product.name} in your basket.")
        else:
            basket.pop(item_id, None)  # Remove the item if quantity is 0
            messages.success(request, f"Removed {product.name} from your basket.")

        request.session['basket'] = basket
        redirect_url = request.POST.get('redirect_url', 'view_basket')  # Default to 'view_basket'
        return redirect(redirect_url)

    except (ValueError, TypeError):
        messages.error(request, "Invalid quantity input.")
        return redirect('view_basket')  # Redirect to view basket


def remove_from_basket(request, item_id):
    """Remove an item from the basket and redirect."""
    basket = request.session.get('basket', {})

    # Get product name for messages
    try:
        product = Product.objects.get(id=item_id)
    except Product.DoesNotExist:
        messages.error(request, "Product does not exist.")
        return redirect('view_basket')  # Redirect to view basket

    if item_id in basket:
        basket.pop(item_id)
        messages.success(request, f"Removed {product.name} from your basket.")
    else:
        messages.error(request, "Item not found in your basket.")

    request.session['basket'] = basket
    return redirect('view_basket')