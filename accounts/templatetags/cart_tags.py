from django import template
from accounts.models import *

register = template.Library()


@register.simple_tag
def number_of_items(request):
    order, created = Order.objects.get_or_create(profile=request.user)
    return order.get_cart_items
