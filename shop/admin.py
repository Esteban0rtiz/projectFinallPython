from django.contrib import admin
from .models import Shop

# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Shop, ShopAdmin)
