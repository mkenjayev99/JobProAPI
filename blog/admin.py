from django.contrib import admin
from .models import Tag, Category, SubContent, Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'image', 'author', 'category', 'date_created', 'date_modified']
    list_display_links = ['id', 'title', 'content', 'author', 'category']
    search_fields = ['title', 'content', 'author', 'category']
    list_filter = ['author', 'category', 'date_created', 'date_modified']
    date_hierarchy = 'date_created'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'text', 'created_date']
    list_display_links = ['id', 'author', 'text']
    search_fields = ['text', 'author']
    list_filter = ['text', 'author']
    date_hierarchy = 'created_date'


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(SubContent)



