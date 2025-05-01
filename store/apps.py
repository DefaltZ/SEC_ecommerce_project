"""
App configuration for the store application.

This module defines the StoreConfig class which configures the store app
with its default settings and metadata.
"""

from django.apps import AppConfig


class StoreConfig(AppConfig):
    """
    Configuration class for the store application.
    
    Attributes:
        default_auto_field: The default field type for auto-incrementing primary keys
        name: The name of the application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
