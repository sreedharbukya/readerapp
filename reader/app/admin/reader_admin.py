from django.contrib import admin

from app.models.reader import Reader


class ReaderAdmin(admin.ModelAdmin):
	list_display = ('id', 'first_name', 'last_name', 'username', 'is_active')
	list_filter = ('id', 'username', 'is_active')
	search_fields = ('id', 'username')


admin.site.register(Reader, ReaderAdmin)
