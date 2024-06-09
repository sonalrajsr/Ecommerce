from django.contrib import admin
from products.models import Featured_Product, New_arrival


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'price', 'rating', 'image')


admin.site.register(Featured_Product, ProductAdmin)

admin.site.register(New_arrival, ProductAdmin)
