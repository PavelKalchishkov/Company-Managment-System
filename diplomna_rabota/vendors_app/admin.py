from django.contrib import admin
from .models import Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number')
    search_fields = ('first_name', 'phone_number')
    ordering = ('first_name',)

admin.site.register(Vendor, VendorAdmin)