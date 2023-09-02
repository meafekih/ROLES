# yourapp/models.py

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import Permission

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('seller', 'Seller')])

    def __str__(self) -> str:
        return f'{self.user} : {self.role}'

class Customer(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

    class Meta:
        permissions = [
            ("can_add_customer", "Can Add Customer"),
            ("can_view_customer", "Can View Customer"),
            # Define more permissions as needed
        ]