from django.urls import path
from .views import machine_learning_view

urlpatterns = [
    path("register/", machine_learning_view, name="machine_learning"),
]
