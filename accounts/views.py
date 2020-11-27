from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import *
from .models import *


@unauthenticated_user
def register_view(request):
    form = UserCreateForm()
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Adding a Profile to User
            username = form.cleaned_data.get('username')
            Profile.objects.create(
                user=user,
                name=user.username,
                email=user.email,
            )
            # Adding a Shopping Cart to User
            ShoppingCart.objects.create(
                user=user,
            )
            # Adding a Group to a User
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            # Success Message
            messages.success(request, "Account created for '" + username + "'")
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect(reverse('accounts:register'))

    context = {
        'form': form,
    }
    return render(request, "register.html", context)


@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:user-home'))
        else:
            messages.error(request, "Invalid Username or Password")
            return HttpResponseRedirect(reverse('accounts:login'))

    return render(request, "login.html", {})


def logout_view(request):
    logout(request)
    return render(request, "index.html")


# @allowed_users(allowed_roles=['admin', 'customer']) (Unused)
@login_required(login_url='home-page')
def user_home_view(request):
    return render(request, "user_home.html", {})


# Admin User Interface (Unused)
@login_required(login_url='/account/login/')
@admin_only
def admin_view(request):
    return render(request, "admin.html", {})


# Shopping Cart
@login_required(login_url='home-page')
def cart_view(request):
    items = ListItem.objects.filter(user=request.user)
    if request.method == "POST":
        delete_item = request.POST.get("remove-item")
        ListItem.objects.filter(user=request.user).filter(
            product=delete_item).delete()
        return HttpResponseRedirect(reverse('accounts:cart'))

    context = {
        'items': items,
    }
    return render(request, "cart.html", context)


# Adding 1 to QTY
@login_required(login_url='home-page')
def add_view(request):
    if request.method == "POST":
        item_id = request.POST.get('product-qty')
        cart = ShoppingCart.objects.get(user=request.user)
        product = Product.objects.get(id=item_id)
        ListItem.objects.create(
            user=request.user, shoppingcart=cart, product=product)
    return HttpResponseRedirect(reverse('accounts:cart'))


# Removing 1 from QTY
@login_required(login_url='home-page')
def remove_view(request):
    if request.method == "POST":
        item_id = request.POST.get('product-qty')
        ListItem.objects.get(id=item_id).delete()
    return HttpResponseRedirect(reverse('accounts:cart'))


# Cart Checkout
@login_required(login_url='home-page')
def checkout_view(request):
    shipping_form = ShippingInfoForm()
    payment_form = PaymentInfoForm()
    items = ListItem.objects.filter(user=request.user)
    total_price = 0
    for item in items:
        total_price += item.product.price
    context = {
        'shipping_form': shipping_form,
        'payment_form': payment_form,
        'total_price': total_price,
    }
    return render(request, "checkout.html", context)
