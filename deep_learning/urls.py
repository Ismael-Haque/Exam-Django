from django.urls import path
from .views import deep_learning_table_view

urlpatterns = [
    path("table/", deep_learning_table_view, name="table"),
]
