from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models
from pages.models import *



# Adding Profile to User
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)



# Placing an Order (Shopping Cart)
class Order(models.Model):
    STATUS = (
        ('Shopping', 'Shopping'),
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.status)

    @property
    def get_cart_items(self):
        listitems = self.listitem_set.all()
        total = sum([item.quantity for item in listitems])
        return total 

    @property
    def get_cart_total(self):
        listitems = self.listitem_set.all()
        total = sum([item.get_total for item in listitems])
        return total



# Shopping Cart Items
class ListItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
