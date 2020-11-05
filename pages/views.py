from django.shortcuts import render
from django.urls import reverse


def home_view(request):
    context = {}
    return render(request, "index.html", context)


def games_view(request):
    context = {}
    return render(request, "games.html", context)
