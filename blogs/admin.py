from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'count_views')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('count_views',)
