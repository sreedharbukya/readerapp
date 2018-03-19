from django.contrib import admin

from app.models import BookOverAllRating


class BookOverAllRatingAdmin(admin.ModelAdmin):
	list_display = ('id', 'total_sum', 'total_count')
	
	list_filter = ('id', )


admin.site.register(BookOverAllRating, BookOverAllRatingAdmin)
