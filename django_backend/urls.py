from django.urls import path
from .views import django_backend_view

urlpatterns = [
    path("conditional-example/", django_backend_view, name="django_backend"),
]
