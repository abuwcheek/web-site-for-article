from django.contrib import admin
from .models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
     list_display = ('name', 'created_at', 'is_active')
     list_display_links = ('name', 'created_at')
     list_filter = ('name', 'created_at')
     search_fields = ('name', 'created_at')
     prepopulated_fields = {'slug': ['name']}

class ArticleAdmin(admin.ModelAdmin):
     list_display = ('author', 'title', 'views', 'created_at', 'is_active')
     list_display_links = ('author', 'title')
     list_filter = ('author', 'created_at')
     search_fields = ('author', 'title', 'created_at')
     prepopulated_fields = {'slug': ['title']}
     readonly_fields = ['views']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)