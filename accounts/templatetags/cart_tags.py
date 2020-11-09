from django import template
from accounts.models import *

register = template.Library()


@register.simple_tag
def number_of_items(request):
    return ListItem.objects.filter(user=request.user).count()
