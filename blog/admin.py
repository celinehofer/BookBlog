from django.contrib import admin
from blog.models import Book, Comment


class BookAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)
