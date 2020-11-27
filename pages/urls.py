from django.urls import path, include
from .views import *

app_name = 'pages'
urlpatterns = [
    path('', home_view, name="home-page"),
    path('shop/', shop_view, name="shop"),
    path('shop/<int:num>/', product_view, name="products"),
]
