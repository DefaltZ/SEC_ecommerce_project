"""
URL configuration for the e-commerce project.

This module defines the root URL patterns for the entire Django project.
It includes the admin interface URLs and includes the store app's URLs.

URL Patterns:
    - 'admin/': Django admin interface
    - '': Includes all URLs from the store app

Media Files:
    In DEBUG mode, this configuration also serves media files from the MEDIA_ROOT directory
    at the MEDIA_URL path. This is for development purposes only and should not be used
    in production.

Configuration:
    - Uses Django's admin site for administrative interface
    - Includes store app URLs for product and category views
    - Configures media file serving in development mode
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
