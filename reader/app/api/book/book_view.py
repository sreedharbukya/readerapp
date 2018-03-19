import ast
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.api.constants import APPLICATION_JSON
from app.core.decorators import reader_login_required
from app.models import BookReview
from app.models.book import Book


class BookAPIView(View):
	@method_decorator(csrf_exempt)
	@method_decorator(reader_login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(BookAPIView, self).dispatch(request, *args, **kwargs)
	
	def post(self, request, **kwargs):
		try:
			request_data = json.loads(request.body)
			
			isbn_number = request_data.pop('isbn_number', None)
			
			if isbn_number and len(isbn_number) is not 13:
				data = {
					"message": "ISBN number is expected to 13 characters only",
					"status": 400
				}
				return HttpResponse(json.dumps(data), status=400, content_type=APPLICATION_JSON)
			
			book = Book(**request_data)
			book.isbn_number = isbn_number
			
			book.created_by = request.reader
			
			book.save()
			
			return HttpResponse(json.dumps(book.to_dict(), cls=DjangoJSONEncoder), content_type=APPLICATION_JSON,
			                    status=201)
		
		except Exception as ex:
			data = {
				"message": "Invalid/Duplicate Data.{}".format(ex.message),
				"status": 400
			}
			return HttpResponse(json.dumps(data), content_type=APPLICATION_JSON, status=400)
	
	def get(self, request, **kwargs):
		
		
		try:
			
			current_reader = request.reader
		
			
			reviewed = request.GET.get('reviewed', None)
			
			owned = request.GET.get('owned', None)
			
			print ("Owned {}".format(owned))
			
			books = []
			
			if reviewed:
				reviewed = ast.literal_eval(reviewed)
				if reviewed:
					reviews_book_ids = BookReview.objects.filter(review_by=current_reader).values_list('book__id')
					books = Book.objects.filter(id__in=reviews_book_ids).exclude(created_by=current_reader)
			
			elif owned and not reviewed:
				owned = ast.literal_eval(owned)
				if owned:
					books = Book.objects.filter(created_by=current_reader)
			else:
				reviews_book_ids = BookReview.objects.filter(review_by=current_reader).values_list('book__id')
				books = Book.objects.all().exclude(created_by=current_reader).exclude(id__in=reviews_book_ids)
			
			data_list = [book.to_details() for book in books if book]
			
			return HttpResponse(json.dumps(data_list, cls=DjangoJSONEncoder), content_type=APPLICATION_JSON, status=200)
		
		except Exception as ex:
			print (ex)
			data = {
				"message" : "Internal Server Error",
				"stauts": 500
			}
			return HttpResponse(json.dumps(data), content_type=APPLICATION_JSON, status=500)
	
