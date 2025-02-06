"""
WSGI config for django_proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# DEBUGGING: Print sys.path to check where Python is searching for modules
print("Python sys.path:", sys.path)

# Try importing settings directly to see if it exists
try:
    import django_proj.settings  # ✅ Explicitly import settings
    print("✅ Django settings module found!")
except ModuleNotFoundError as e:
    print("❌ Error: Could not import settings:", e)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_proj.settings")

application = get_wsgi_application()

