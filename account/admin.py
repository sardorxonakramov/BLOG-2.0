from django.contrib import admin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'age', 'created_at']
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['age', 'created_at']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)