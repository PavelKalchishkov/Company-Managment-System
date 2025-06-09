from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'length', 'weight', 'color', 'vendor')
    search_fields = ('name', 'price')
    ordering = ('name',)

admin.site.register(Product, ProductAdmin)