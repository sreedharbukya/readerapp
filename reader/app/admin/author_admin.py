from django.contrib import admin

from app.models import Author


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('id','first_name', 'last_name')
	list_filter = ('id', 'first_name')
	
	


admin.site.register(Author, AuthorAdmin)


