from django.contrib import admin

from apps.news.models import News, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'published_at', 'created_at']
    list_filter = ['author', 'category', 'published_at']
    search_fields = ['title', 'author', 'category']
    prepopulated_fields = {'slug': ['title']}
    date_hierarchy = 'published_at'