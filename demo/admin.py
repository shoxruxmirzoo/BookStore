from django.contrib import admin
from .models import Book, BookNumber, Character, Author


# Register your models here.


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['price']
    search_fields = ['title', 'description']


admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)
