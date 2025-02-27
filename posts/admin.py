from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['created_at']
    list_per_page = 10
admin.site.register(Post, PostAdmin)