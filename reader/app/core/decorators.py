import json
import logging

from django.core.signing import TimestampSigner
from django.http import HttpResponse

from app.api.constants import APPLICATION_JSON
from app.models.reader import Reader

logger = logging.getLogger(__name__)


def reader_login_required(function):
	def auth_required_response():
		data = {
			"message": "Login Required",
			"status_code": 401
		}
		return HttpResponse(json.dumps(data), status=401, content_type=APPLICATION_JSON)
	
	def check_validity_cookie(auth_cookie):
		try:
			signer = TimestampSigner()
			unsigned_value = signer.unsign(auth_cookie, max_age=1800)
			return True, unsigned_value
		
		except Exception as ex:
			return False, None
	
	def check_username(username):
		
		return Reader.objects.get(username=username, is_active=True)
	
	def wrapped_view(request, *args, **kwargs):
		
		auth_cookie = request.COOKIES.get('auth')
		
		if auth_cookie:
			
			status, unsigned_value = check_validity_cookie(auth_cookie)
			
			if status and unsigned_value:
				
				try:
					reader = check_username(unsigned_value)
					
					request.reader = reader
					
					return function(request, *args, **kwargs)
				
				except Reader.DoesNotExist:
					return auth_required_response()
			
			else:
				return auth_required_response()
		
		else:
			return auth_required_response()
	
	return wrapped_view
