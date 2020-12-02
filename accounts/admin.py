from django.contrib import admin
from .models import *
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline


# Profile - Order - ListItems (Nested)
class ListItemInline(NestedTabularInline):
    model = ListItem
    extra = 0

class OrderInline(NestedTabularInline):
    model = Order
    readonly_fields = ('transaction_id',)
    extra = 0
    inlines = [ListItemInline]

class ProfileAdmin(NestedModelAdmin):
    list_display = ('user', 'name', 'email')
    search_fields = ('name', 'email')
    readonly_fields = ('user', 'name', 'email')
    inlines = [OrderInline]
    
admin.site.register(Profile, ProfileAdmin)


# Order Inline
class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'date_created', 'transaction_id')
    list_filter = ('status', 'date_created')
    readonly_fields = ('profile', 'transaction_id',)
    search_fields = ('transaction_id',)
    inlines = [ListItemInline]

admin.site.register(Order, OrderAdmin)


# Registered Models
# admin.site.register(ListItem)
admin.site.register(Product)
admin.site.register(Tag)


