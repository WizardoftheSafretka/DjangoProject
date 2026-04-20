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



