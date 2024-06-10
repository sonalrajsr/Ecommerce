# home/admin.py
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'user', 'product', 'confermed', 'created_at')
    list_filter = ('confermed', 'created_at')
    search_fields = ('user__username', 'product__name')

admin.site.register(Order, OrderAdmin)
