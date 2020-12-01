from django.contrib import admin
from .models import *
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline


# admin.site.register(Model)


# Profile - Order - ListItems (Nested)
class ListItemInline(NestedTabularInline):
    model = ListItem
    extra = 0

# @admin.register(Order)
class OrderInline(NestedTabularInline):
    model = Order
    # Order.objects.exclude(status="Shopping")
    extra = 0
    inlines = [ListItemInline]

# @admin.register(Profile)
class ProfileAdmin(NestedModelAdmin):
    inlines = [OrderInline]
    

admin.site.register(Profile, ProfileAdmin)



# Registering Models
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(ListItem)


