"""
URL configuration for the store app.

This module defines the URL patterns for the store application, mapping URLs to view functions.
The app_name variable is used for namespacing the URLs.

URL Patterns:
    - '' (homepage): Displays all available products
    - 'category/<slug:category_slug>/': Displays products filtered by category
    - 'product/<slug:product_slug>/': Displays detailed information about a specific product
"""

from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='category_detail'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
]