"""
ASGI (Asynchronous Server Gateway Interface) configuration for the e-commerce project.

This module configures the ASGI application for the Django project, enabling asynchronous
web server capabilities. It sets up the application to handle WebSocket connections and
other asynchronous protocols.

The module exposes the ASGI callable as a module-level variable named ``application``,
which is used by ASGI servers to serve the Django application.

Configuration:
    - Sets the default Django settings module to 'ecommerce_project.settings'
    - Creates an ASGI application using Django's get_asgi_application()

For more information on ASGI configuration, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')

application = get_asgi_application()
