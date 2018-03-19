import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.api.constants import APPLICATION_JSON
from app.core.decorators import reader_login_required
from app.models import BookReview, Book


class BookReviewAPIView(View):
	@method_decorator(csrf_exempt)
	@method_decorator(reader_login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(BookReviewAPIView, self).dispatch(request, *args, **kwargs)
	
	def post(self, request, *args, **kwargs):
		try:
			current_reader = request.reader
			
			isbn_number = self.kwargs.get('isbn_number')
			
			book = Book.objects.get(isbn_number=isbn_number)
			
			if book.created_by is current_reader:
				data = {
					"message": "You can't rate the book which you created",
					"status": 400
				}
				return HttpResponse(json.dumps(data), status=400, content_type=APPLICATION_JSON)
			
			request_data = json.loads(request.body)
			
			existing = BookReview.objects.filter(book__isbn_number=isbn_number, review_by=current_reader).exists()
			
			if existing:
				data = {
					"message": "You have already rated this book",
					"status": 400
				}
				return HttpResponse(json.dumps(data), status=400, content_type=APPLICATION_JSON)
			
			book_review = BookReview(**request_data)
			book_review.book = book
			
			book_review.review_by = current_reader
			
			book_review.save()
			
			return HttpResponse(json.dumps(book_review.to_dict(), cls=DjangoJSONEncoder), status=201,
			                    content_type=APPLICATION_JSON)
		
		except Book.DoesNotExist as ex:
			data = {
				"message": "Book doesn't exists to review",
				"status": 400
			}
			return HttpResponse(json.dumps(data), status=400, content_type=APPLICATION_JSON)
		
		
		except Exception as ex:
			print (ex)
			data = {
				"message": "Invalid Review details",
				"status": 500
			}
			return HttpResponse(json.dumps(data), status=500, content_type=APPLICATION_JSON)
	
	def get(self, request, *args, **kwargs):
		
		try:
			current_reader = request.reader
			
			isbn_number = self.kwargs.get('isbn_number')
			
			book = Book.objects.get(isbn_number=isbn_number)
			
			book_reviews = BookReview.objects.filter(book=book)
			
			data_list = [review.to_dict() for review in book_reviews if review]
			
			return HttpResponse(json.dumps(data_list, cls=DjangoJSONEncoder), status=200, content_type=APPLICATION_JSON)
		
		except Book.DoesNotExist:
			data = {
				"message": "Book doesn't exists to review",
				"status": 400
			}
			return HttpResponse(json.dumps(data), status=400, content_type=APPLICATION_JSON)
		
		
		except Exception as ex:
			data = {
				"message": "Something went wrong, try again later",
				"status": 500
			}
			return HttpResponse(json.dumps(data), status=500, content_type=APPLICATION_JSON)
