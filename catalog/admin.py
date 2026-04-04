from gettext import Catalog

from django.contrib import admin

from blogs.models import Blog
from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "name", 'price', 'category')
    list_filter = ('category',)
    search_fields = ("name", "description")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', "name")
    search_fields = ("name", "description")

@admin.register(Blog)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'count_views')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('count_views',)

