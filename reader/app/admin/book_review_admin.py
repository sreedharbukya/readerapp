from django.contrib import admin

from app.models import BookReview


class BookReviewAdmin(admin.ModelAdmin):
	list_display = ('id', 'book', 'rating', 'review_by', 'comment')
	list_filter = ('id', 'rating')
	search_fields = ('book__isbn_number', 'book__title')
	
	
	
admin.site.register(BookReview, BookReviewAdmin)
