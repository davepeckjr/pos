from django.contrib import admin

from .models import Order, OrderItem, MenuItem, YouPickTwo, Ingredients

admin.site.register(Order, OrderItem)
admin.site.register(MenuItem, YouPickTwo)
admin.site.register(Ingredients)