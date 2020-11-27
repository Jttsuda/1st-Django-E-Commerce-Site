from django.shortcuts import render
from django.urls import reverse
from accounts.decorators import unauthenticated_user
from django.contrib import messages
from .models import *
from accounts.models import *


@unauthenticated_user
def home_view(request):
    context = {}
    return render(request, "index.html", context)


# Shop View
def shop_view(request):
    products = Product.objects.all()
    tags = Tag.objects.all()
    context = {
        'products': products,
        'tags': tags,
    }
    return render(request, "shop.html", context)


# Adding Product to Shopping Cart (Product Page)
def product_view(request, num):
    product = Product.objects.get(id=num)
    if request.method == "POST":
        if request.user.is_authenticated:
            if ListItem.objects.filter(user=request.user).count() < 40:
                cart = ShoppingCart.objects.get(user=request.user)
                add_number = int(request.POST.get("numberToAdd"))
                for number in range(add_number):
                    ListItem.objects.create(
                        user=request.user, shoppingcart=cart, product=product)
                messages.success(request, "Added to Cart")
            else:
                messages.error(
                    request, "Please checkout first before adding more Items.")
        else:
            messages.error(request, "Register/Login Before Adding Items")

    context = {
        "product": product,
    }
    return render(request, "product.html", context)
