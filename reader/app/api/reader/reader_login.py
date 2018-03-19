import json

from django.core.serializers.json import DjangoJSONEncoder
from django.core.signing import TimestampSigner
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.api.constants import APPLICATION_JSON, AUTH_COOKIE_NAME
from app.models import Reader


class ReaderLogin(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(ReaderLogin, self).dispatch(request, *args, **kwargs)
	
	def post(self, request, **kwargs):
		try:
			request_data = json.loads(request.body)
			username = request_data.get('username', None)
			
			if username:
				reader = self.check_authentication(username)
				
				if not reader.is_active:
					data = {
						"message": "Inactive User",
						"status": 401
					}
					return HttpResponse(json.dumps(data), content_type=APPLICATION_JSON, status=401)
				
				response = HttpResponse(content_type=APPLICATION_JSON)
				
				signed_value = self.prepare_cookie(username)
				response.set_cookie(AUTH_COOKIE_NAME, signed_value, expires=1800)
				response.content = json.dumps(reader.to_dict(), cls=DjangoJSONEncoder)
				response.status_code = 200
				
				return response
			
			else:
				raise Exception("Username is empty")
		
		except Reader.DoesNotExist:
			data = {
				"message": "Invalid Credentials",
				"status": 401
			}
			return HttpResponse(json.dumps(data), content_type=APPLICATION_JSON, status=401)
		
		
		
		except Exception as ex:
			print (ex)
			data = {
				"message": "Error- {}".format(ex.message),
				"status": 500
			}
			return HttpResponse(json.dumps(data), content_type=APPLICATION_JSON, status=401)
	
	def check_authentication(self, username):
		
		return Reader.objects.get(username=username)
	
	def prepare_cookie(self, username):
		timed_signer = TimestampSigner()
		
		singed_value = timed_signer.sign(username)
		
		return singed_value
