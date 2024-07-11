from django.contrib import admin
from .models import Book, Product

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'author', 'price',)
    ordering = ('id',)


admin.site.register(Book, BookAdmin)


class ProductAdmin(admin.ModelAdmin):
    List_display = ('id', 'title', 'action', 'image',)
    ordering = ('id',)

admin.site.register(Product, ProductAdmin)