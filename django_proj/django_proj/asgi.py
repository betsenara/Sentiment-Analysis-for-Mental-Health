"""
ASGI config for django_proj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_proj.settings")

application = get_asgi_application()

"""

# django_project/asgi.py
import os
from django.core.asgi import get_asgi_application
from myapp.fastapi import app  # Correct reference
from fastapi.middleware.wsgi import WSGIMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_proj.settings")

# Initialize Django ASGI app
django_application = get_asgi_application()

# Mount Django under FastAPI
app.mount("/django", WSGIMiddleware(django_application))

# Set FastAPI as the main ASGI app
application = app


