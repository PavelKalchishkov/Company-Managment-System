from django.contrib import admin
from .models import Invoice, Company

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'DDS', 'date', 'comment', 'discount', 'whole_price_without_dds',
                    'whole_price_with_dds','cancelled','company', 'order')
    search_fields = ('comapany', 'order')
    ordering = ('company',)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'eik' ,'dds' , 'name', 'address', 'mol', 'recipient')
    search_fields = ('eik','name')
    ordering = ('id','eik', 'name')

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Company, CompanyAdmin)
