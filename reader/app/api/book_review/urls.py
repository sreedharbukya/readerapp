from django.conf.urls import url

from app.api.book_review.book_review import BookReviewAPIView

urlpatterns = [
	url(r'', BookReviewAPIView.as_view(), name="book_review"),

]
