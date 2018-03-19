import logging

from django.core.signing import TimestampSigner
from django.utils.deprecation import MiddlewareMixin

from app.api.constants import AUTH_COOKIE_NAME

logger = logging.getLogger(__name__)


class SessionAuthCookieMiddleWare(MiddlewareMixin):
	def process_request(self, request):
		auth_cookie = request.COOKIES.get('auth')
		pass
	
	def process_response(self, request, response):
		auth_cookie = request.COOKIES.get(AUTH_COOKIE_NAME)
		
		if hasattr(request, 'reader') and auth_cookie:
			signed_value = self.update_cookie(request.reader)
			response.set_cookie(AUTH_COOKIE_NAME, signed_value, expires=1800)
			logging.debug("Updated cookie value once again")
		
		response['Access-Control-Allow-Headers'] = 'Content-Type'
		return response
	
	def update_cookie(self, reader):
		timed_signer = TimestampSigner()
		
		singed_value = timed_signer.sign(reader.username)
		
		return singed_value
