from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    # path('admin/', admin_view, name="admin"),
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('home/', user_home_view, name="user-home"),
    path('cart/', cart_view, name="cart"),
    path('add/', add_view, name="add"),
    path('remove/', remove_view, name="remove"),
    path('checkout/', checkout_view, name="checkout"),
    path('order/', order_view, name="order"),
]
