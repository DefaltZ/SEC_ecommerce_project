# store/admin.py

"""
Admin configuration for the store app.

This module registers the Category and Product models with the Django admin interface
and configures their display and behavior in the admin panel.
"""

from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.
    
    Attributes:
        list_display: Fields to display in the list view
        prepopulated_fields: Fields that are automatically populated based on other fields
        search_fields: Fields that can be searched in the admin interface
        ordering: Default ordering of records
    """
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    ordering = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Product model.
    
    Attributes:
        list_display: Fields to display in the list view
        list_filter: Fields that can be used to filter the list
        list_editable: Fields that can be edited directly in the list view
        prepopulated_fields: Fields that are automatically populated based on other fields
        search_fields: Fields that can be searched in the admin interface
        date_hierarchy: Field used for date-based navigation
        ordering: Default ordering of records
    """
    list_display = ['name', 'category', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    date_hierarchy = 'created'
    ordering = ['name']