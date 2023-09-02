# yourapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add_customer/', views.add_customer, name='add_customer'),
    path('view_customer/<int:customer_id>/', views.view_customer, name='view_customer'),
]
