from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models


# Adding Profile to User
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# Products
class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(null=True, blank=True, upload_to="")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


# Customer Orders
# Shopping Cart
class ListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    shoppingcart = models.ForeignKey(
        ShoppingCart, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


# Placing an Order
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered'),
    )
    profile = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)
