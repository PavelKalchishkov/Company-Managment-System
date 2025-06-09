from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','phone_number','email','is_active', 'is_staff')
    list_display_links = ('username',)
    ordering = ('is_active', 'username')

admin.site.register(CustomUser, CustomUserAdmin)