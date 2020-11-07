from django.contrib.auth.models import User
from django.db import models

# Adding to Base User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


# Products
class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name

# Adding Products to Shopping Cart


class ListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    shoppingcart = models.ForeignKey(
        ShoppingCart, on_delete=models.CASCADE, null=True)
    product = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.product
