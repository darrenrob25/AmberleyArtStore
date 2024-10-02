from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProductForm
from products.models import Product

def product_list(request):
    """Display a list of products."""
    products = Product.objects.all()
    return render(request, 'product_admin/product_list.html', {'products': products})

def add_product(request):
    """Add a new product."""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'product_admin/add_product.html', {'form': form})

def edit_product(request, product_id):
    """Edit an existing product."""
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product_admin/edit_product.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    """Delete a product."""
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('product_list')