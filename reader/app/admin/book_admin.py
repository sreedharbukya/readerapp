from django.contrib import admin

from app.models.book import Book


class BookAdmin(admin.ModelAdmin):
	list_display = ('id', 'isbn_number', 'title', 'created_by')
	list_filter = ('isbn_number', 'author', 'created_by')
	search_fields = ('isbn_number', 'title')
	


admin.site.register(Book, BookAdmin)
