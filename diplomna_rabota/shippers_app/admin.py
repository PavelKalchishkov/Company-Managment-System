from django.contrib import admin
from .models import Shipper

# Register your models here.
class ShipperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'salary')
    search_fields = ('name', 'phone_number')
    ordering = ('name',)

admin.site.register(Shipper, ShipperAdmin)