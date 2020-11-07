from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import UserCreateForm
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


# @allowed_users(allowed_roles=['admin', 'customer'])
@login_required(login_url='home-page')
def user_home_view(request):
    return render(request, "user_home.html", {})


@login_required(login_url='/account/login/')
@admin_only
def admin_view(request):
    return render(request, "admin.html", {})


# Shopping
def shop_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, "shop.html", context)


def product_view(request, num):
    product = Product.objects.get(id=num)
    context = {
        "product": product,
    }
    return render(request, "product.html", context)
