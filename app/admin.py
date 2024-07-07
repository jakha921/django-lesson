from django.contrib import admin

from .models import Category, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'category')
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    search_fields = ('title', 'content')
    ordering = ('status', 'created_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)
    ordering = ('name',)
