from django.contrib import admin
from .models import Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'additional_information')
    search_fields = ('name', 'phone_number')
    ordering = ('name',)

admin.site.register(Vendor, VendorAdmin)