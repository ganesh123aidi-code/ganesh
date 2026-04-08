from django.contrib import admin
from .models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from title             
    list_display = ('title', 'category', 'author', 'status', 'featured_post', 'created_at')  # Display these fields in the admin list view
    search_fields = ('title', 'category__name', 'author', 'status')  # Enable search by these fields
    list_editable = ('status', 'featured_post')  # Allow changing status and featured_post from the list view
    
# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)