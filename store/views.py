from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    """
    Display a list of products, optionally filtered by category.
    
    Args:
        request: HTTP request object
        category_slug (str, optional): Slug of the category to filter products
    
    Returns:
        HttpResponse: Rendered template with the following context:
            - category: Current category object (if filtered)
            - categories: QuerySet of all categories
            - products: QuerySet of products (filtered if category specified)
    
    Template:
        store/product_list.html
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'store/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, product_slug):
    """
    Display detailed information about a specific product.
    
    Args:
        request: HTTP request object
        product_slug (str): Slug of the product to display
    
    Returns:
        HttpResponse: Rendered template with the following context:
            - product: Product object
    
    Template:
        store/product_detail.html
    
    Raises:
        Http404: If the product is not found or not available
    """
    product = get_object_or_404(Product, slug=product_slug, available=True)
    return render(request, 'store/product_detail.html', {'product': product})