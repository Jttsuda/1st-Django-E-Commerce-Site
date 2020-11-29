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
            user_order, created = Order.objects.get_or_create(profile=request.user)
            if ListItem.objects.filter(order=user_order).count() < 40:
                add_number = int(request.POST.get("numberToAdd"))
                add_product, created = ListItem.objects.get_or_create(order=user_order, product=product)
                add_product.quantity = (add_product.quantity + add_number)
                add_product.save()
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
