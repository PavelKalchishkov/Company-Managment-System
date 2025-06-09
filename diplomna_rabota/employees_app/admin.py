from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'age', 'brute_salary')
    search_fields = ('name', 'phone_number')
    ordering = ('name',)

admin.site.register(Employee, EmployeeAdmin)