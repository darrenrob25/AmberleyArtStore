from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Review
from .forms import ReviewForm

def all_products(request):
    """ A view to show all products with category filtering """
    # Get distinct categories from the Product model
    categories = Product.objects.values_list('category', flat=True).distinct()

    # Get the selected category from the GET request
    selected_category = request.GET.get('category')

    # If a category is selected, filter products by that category
    if selected_category:
        products = Product.objects.filter(category=selected_category)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }

    return render(request, 'products/products.html', context)
    

def product_detail(request, product_id):
    """ A view to show individual products with reviews """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            if request.user.is_authenticated:
                review.user = request.user
            review.save()
            messages.success(request, "Your review has been added successfully!")
            return redirect('product_detail', product_id=product.id)  # Redirect to see the new review
    else:
        form = ReviewForm()

    reviews = product.reviews.all()  # Use the related name 'reviews'

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)

def edit_review(request, review_id):
    """ A view to edit existing reviews """
    review = get_object_or_404(Review, pk=review_id)
    product = review.product  # Get the product associated with the review

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)  # Bind the form to the existing review
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been updated successfully!")
            return redirect('product_detail', product_id=product.id)  # Redirect to the product detail page
    else:
        form = ReviewForm(instance=review)  # Populate the form with the review's current data

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/edit_review.html', context)  # Create a template for this

def delete_review(request, review_id):
    """ A view to delete a review """
    review = get_object_or_404(Review, pk=review_id)

    # Check if the user is authenticated
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to delete a review.")
        return redirect('product_detail', product_id=review.product.id)

    # Check if the user is the owner of the review or a staff member
    if review.user == request.user or request.user.is_staff:
        review.delete()
        messages.success(request, "Review deleted successfully.")
    else:
        messages.error(request, "You do not have permission to delete this review.")

    return redirect('product_detail', product_id=review.product.id)