import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.api.constants import APPLICATION_JSON, AUTH_COOKIE_NAME
from app.core.decorators import reader_login_required


class ReaderLogout(View):
	@method_decorator(csrf_exempt)
	@method_decorator(reader_login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(ReaderLogout, self).dispatch(request, *args, **kwargs)
	
	def get(self, request, *args, **kwargs):
		response = HttpResponse(content_type=APPLICATION_JSON)
		
		if request.COOKIES.get(AUTH_COOKIE_NAME):
			response.delete_cookie(AUTH_COOKIE_NAME)
			
		data = {
			"message" : "Successful logout",
			"status" : 200
			
		}
		response.content = json.dumps(data)
		
		return response
