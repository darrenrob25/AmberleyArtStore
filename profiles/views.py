from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from checkout.models import PurchaseOrder
from .models import UserProfile
from .forms import UserProfileForm

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, default_user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)

    # Fetch orders associated with the logged-in user's profile
    orders = PurchaseOrder.objects.filter(user_profile=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)

def order_history(request, order_number):
    """Display the details of a specific order."""
    order = get_object_or_404(PurchaseOrder, order_id=order_number, customer_email=request.user.email)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'  # Adjust this template if necessary
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)