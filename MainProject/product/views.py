from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Laptop, Category, Brand

def all_laptops_view(request):
    # Get filter parameters
    brand_ids = request.GET.getlist('brand')  # Get selected brands from the URL
    category_ids = request.GET.getlist('category')  # Get selected categories from the URL
    min_price = request.GET.get('min_price', 0)  # Default minimum price
    max_price = request.GET.get('max_price', 100000)  # Default maximum price

    # Filter laptops based on parameters
    laptops = Laptop.objects.filter(price__gte=min_price, price__lte=max_price)
    if brand_ids:
        laptops = laptops.filter(brand__id__in=brand_ids)
    if category_ids:
        laptops = laptops.filter(category__id__in=category_ids)

    # Pagination
    paginator = Paginator(laptops, 6)  # Show 6 laptops per page
    page_number = request.GET.get('page')  # Get current page number from URL
    page_obj = paginator.get_page(page_number)

    # Fetch all brands and categories for filters
    brands = Brand.objects.all()
    categories = Category.objects.all()

    # Pass data to the template
    context = {
        'page_obj': page_obj,  # Paginated laptops
        'brands': brands,  # All brands
        'categories': categories,  # All categories
        'selected_brands': list(map(int, brand_ids)),  # Selected brands as integers
        'selected_categories': list(map(int, category_ids)),  # Selected categories as integers
        'min_price': min_price,  # Current minimum price
        'max_price': max_price,  # Current maximum price
    }
    return render(request, 'product/shop.html', context)






def search_product(request):
    query = request.GET.get('q', '').strip()  # Get search query
    laptops = Laptop.objects.filter(name__icontains=query) if query else Laptop.objects.none()  # Filter bikes by name
    laptops = Laptop.objects.filter(description__icontains=query) if query else Laptop.objects.none()  # Filter bikes by name


    # Pagination for search results
    paginator = Paginator(laptops, 6)  # Show 6 bikes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Fetch all brands, categories, and colors for filters
    brands = Brand.objects.all()
    categories = Category.objects.all()

    return render(request, 'product/shop.html', {
        'page_obj': page_obj,
        'brands': brands,
        'categories': categories,
        'query': query,  # Pass the query to the template
    })


from django.shortcuts import render, get_object_or_404
from product.models import Laptop

def product_detail(request, product_id):
    # Get the product by ID
    product = get_object_or_404(Laptop, id=product_id)

    # Get similar products based on the brand
    similar_products = Laptop.objects.filter(brand=product.brand).exclude(id=product.id)

    return render(request, 'product/product-single.html', {
        'product': product,
        'similar_products': similar_products,
    })



