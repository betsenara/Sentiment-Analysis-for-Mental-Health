"""
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]

"""

"""
# myapp/urls.py
from django.urls import path
from django.http import HttpResponse
from fastapi.middleware.wsgi import WSGIMiddleware
from .fastapi import app  # Correctly importing app

# Django View
def home_view(request):
    return HttpResponse("<h1>Welcome to Django + FastAPI App</h1>")

# Django URLs
urlpatterns = [
    path("", home_view, name="home"),  # Home route
    path("predict/", predict_view, name="predict"),
]
"""
""" 
from django.urls import path
from .views import count_words_view

urlpatterns = [
    path("count/", count_words_view, name="count_words"),
]
"""
from django.urls import path
from .views import predict_mental_health_view

urlpatterns = [
    path("predict/", predict_mental_health_view, name="predict"),
]


