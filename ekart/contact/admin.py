from django.contrib import admin
from contact.models import Contact
# Register your models here.

class contacAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'order_id', 'subject')


admin.site.register(Contact, contacAdmin)
