# yourapp/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .decorators import admin_required, seller_required

# View accessible by admins
@admin_required
def add_customer(request):
    # Your view logic for adding a customer here
    return HttpResponse('Adding a customer...')

# View accessible by sellers
@seller_required
def view_customer(request, customer_id):
    # Your view logic for viewing a customer here
    return HttpResponse(f'Viewing customer {customer_id}...')

# Example view accessible by all users (no decorator)
def public_view(request):
    # Your view logic for a public view here
    return HttpResponse('This is a public view...')
