from django.contrib import admin
from .models import *
from accounts.models import *

# Register your models here.
# admin.site.register(Model)

# Changing Admin Titles
admin.site.site_header = "Suda's Admin"
admin.site.site_title = "Suda's Admin Portal"
admin.site.index_title = "Welcome to Suda's Researcher Portal"


# Displaying ListItems inside of Shopping Carts for Admin
class ListItemInline(admin.StackedInline):
    model = ListItem


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    inlines = [ListItemInline]
