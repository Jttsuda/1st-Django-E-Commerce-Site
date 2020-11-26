from django.shortcuts import render
from django.urls import reverse
from accounts.decorators import unauthenticated_user


@unauthenticated_user
def home_view(request):
    context = {}
    return render(request, "index.html", context)
