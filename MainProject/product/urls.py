from django.urls import path
from . import views



urlpatterns = [
    path('all-products/', views.all_laptops_view, name='all_products'),
    path('product/product/<int:product_id>/', views.product_detail, name='product'),
    path('search/', views.search_product, name='search_product'),



    # Add any other paths for other views as needed
]