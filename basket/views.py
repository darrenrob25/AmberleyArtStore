from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def view_basket(request):
    """ A view to view your basket """

    return render(request,'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add products to basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Edit the basket."""
    
    # Get the basket from the session
    basket = request.session.get('basket', {})
    
    # Check if the item exists in the basket
    if item_id not in basket:
        # If the item does not exist, you may want to return an error response or redirect
        return HttpResponse(status=404)

    try:
        # Get the quantity from the POST data, default to 0 if not found
        quantity = int(request.POST.get('quantity', 0))

        # If the quantity is greater than 0, update it
        if quantity > 0:
            basket[item_id] = quantity  # Set the new quantity
        else:
            basket.pop(item_id, None)  # Remove the item if quantity is 0

        # Update the session with the modified basket
        request.session['basket'] = basket
        redirect_url = request.POST.get('redirect_url', 'view_basket')  # Default to 'view_basket' if not provided
        return redirect(redirect_url)

    except (ValueError, TypeError):
        # Handle invalid quantity input
        return HttpResponse(status=400)  # Bad request if the quantity isn't valid


def remove_from_basket(request, item_id):
    """Remove an item from the basket and redirect."""
    
    # Get the basket from the session
    basket = request.session.get('basket', {})

    # Safely remove the item from the basket, if it exists
    if item_id in basket:
        basket.pop(item_id)

    # Update the session with the modified basket
    request.session['basket'] = basket

    # Redirect back to the basket view
    return redirect('view_basket')  # Make sure 'view_basket' is the name of your basket view URL