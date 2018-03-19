from django.conf.urls import include, url

urlpatterns = [
	url(r'^author/', include('app.api.author.urls'), name="author"),
	url(r'^reader/', include('app.api.reader.urls'), name="reader"),
	url(r'^book/', include('app.api.book.urls'), name="book"),
	url(r'^review/(?P<isbn_number>[^/]+)/', include('app.api.book_review.urls'), name="book_reviews")

]
