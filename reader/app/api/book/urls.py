from django.conf.urls import url

from app.api.book.book_view import BookAPIView

urlpatterns = [
	url(r'', BookAPIView.as_view(), name="book"),

]
