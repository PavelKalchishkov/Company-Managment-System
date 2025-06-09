from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'address')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')
    ordering = ('first_name','last_name')

admin.site.register(Client, ClientAdmin)