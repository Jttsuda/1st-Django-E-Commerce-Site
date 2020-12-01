from django import template
from accounts.models import *

register = template.Library()


@register.simple_tag
def number_of_items(request):
    order = Order.objects.get(profile=request.user.profile.id, status="Shopping")
    return order.get_cart_items
