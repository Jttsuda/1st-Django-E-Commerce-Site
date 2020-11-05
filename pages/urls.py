from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_view, name="home-page"),
    path('games/', games_view, name="games"),
    path('account/', include('accounts.urls')),
]
