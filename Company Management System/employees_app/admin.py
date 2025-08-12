from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number')
    search_fields = ('first_name', 'phone_number')
    ordering = ('first_name',)

admin.site.register(Employee, EmployeeAdmin)

admin.site.site_header = "Technocenter ood"
admin.site.site_title = "Technocenter ood"
admin.site.index_title = "Technocenter ood"

