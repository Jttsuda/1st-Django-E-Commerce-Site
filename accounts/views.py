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
import datetime



# Admin User Interface
# @login_required(login_url='/account/login/')
# @admin_only
# def admin_view(request):
#     return render(request, "admin.html", {})



# Register
@unauthenticated_user
def register_view(request):
    form = UserCreateForm()
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Adding Profile and Order to User
            username = form.cleaned_data.get('username')
            profile = Profile.objects.create(
                user=user,
                name=user.username,
                email=user.email,
            )
            Order.objects.create(
                profile=profile,
                status="Shopping",
            )
            # Adding Group to a User
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            # Success/Error Message
            messages.success(request, "Account created for '" + username + "'")
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect(reverse('accounts:register'))

    context = {
        'form': form,
    }
    return render(request, "register.html", context)



# Login
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



# Logout
def logout_view(request):
    logout(request)
    return render(request, "index.html")



# User Home
@login_required(login_url='home-page')
def user_home_view(request):
    return render(request, "user_home.html", {})



# Cart View
@login_required(login_url='home-page')
def cart_view(request):
    cart = Order.objects.get(profile=request.user.profile.id, status="Shopping")
    user_order = ListItem.objects.filter(order=cart)
    # Remove Product(s) From Cart
    if request.method == "POST":
        delete_item = request.POST.get("remove-item")
        ListItem.objects.filter(order=cart).filter(
            product=delete_item).delete()
        return HttpResponseRedirect(reverse('accounts:cart'))

    context = {
        'order': cart,
        'items': user_order,
    }
    return render(request, "cart.html", context)



# Adding 1 to QTY
@login_required(login_url='home-page')
def add_view(request):
    if request.method == "POST":
        item_id = request.POST.get('product-qty')
        product = ListItem.objects.get(id=item_id)
        product.quantity += 1
        product.save()
    return HttpResponseRedirect(reverse('accounts:cart'))



# Removing 1 from QTY
@login_required(login_url='home-page')
def remove_view(request):
    if request.method == "POST":
        item_id = request.POST.get('product-qty')
        product = ListItem.objects.get(id=item_id)
        product.quantity -= 1
        product.save()
    if product.quantity <= 0:
        product.delete()
    return HttpResponseRedirect(reverse('accounts:cart'))



# Cart Checkout
@login_required(login_url='home-page')
def checkout_view(request):
    cart = Order.objects.get(profile=request.user.profile.id, status="Shopping")
    shipping_form = ShippingInfoForm()
    payment_form = PaymentInfoForm()

    context = {
        'cart': cart,
        'shipping_form': shipping_form,
        'payment_form': payment_form,
    }
    return render(request, "checkout.html", context)



# Placing an Order
@login_required(login_url='home-page')
def order_view(request):
    profile = Profile.objects.get(user=request.user)
    order = Order.objects.get(profile=request.user.profile.id, status="Shopping")
    # No Pending Order Exists
    if Order.objects.filter(profile=request.user.profile.id, status="Pending").count() == 0:
        order.status = "Pending"
        order.transaction_id = datetime.datetime.now().timestamp()
        order.save()
        Order.objects.create(profile=profile, status="Shopping")
    # Pending Order Exists
    else:
        existing_order = Order.objects.get(profile=request.user.profile.id, status="Pending")
        items = order.listitem_set.all()
        for item in items:
            # Change QTY of Pending Item(s)
            if existing_order.listitem_set.filter(product=item.product.id).count() >= 1:
                chg_qty = existing_order.listitem_set.get(product=item.product.id)
                chg_qty.quantity += item.quantity
                chg_qty.save()
                item.delete()
            # Add Pending Item(s)
            else:
                add_item = ListItem.objects.get(id=item.id)
                existing_order.listitem_set.add(add_item)

    context = {
    }
    return render(request, "order.html", context)
