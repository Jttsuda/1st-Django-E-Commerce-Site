from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('home/', user_home_view, name="user-home"),
    path('shop/', shop_view, name="shop"),
    path('admin/', admin_view, name="admin"),
    path('shop/<int:num>/', product_view, name="products"),
    path('cart/', cart_view, name="cart"),
]
