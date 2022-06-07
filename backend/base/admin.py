from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'brand', 'category', 'price', 'countInStock')


# Register your models here.

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Review)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.ShippingAddress)
