from django.contrib import admin
from .models import Item, Project, Comment, Genre, Status, Part, Chapter

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)
    date_hierarchy = 'date'
    ordering = ('-date',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'date')
    list_filter = ('date',)
    date_hierarchy = 'date'
    ordering = ('-date',)

admin.site.register(Item, ItemAdmin)

admin.site.register(Project)

admin.site.register(Genre)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Status)

admin.site.register(Part)

admin.site.register(Chapter)