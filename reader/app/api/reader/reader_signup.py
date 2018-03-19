import json
import logging

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.api.constants import APPLICATION_JSON
from app.models import Reader

logger = logging.getLogger(__name__)


class ReaderSignup(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(ReaderSignup, self).dispatch(request, **kwargs)
	
	def post(self, request, **kwargs):
		logger.info("Started sign up")
		try:
			request_data = json.loads(request.body)
			
			reader = Reader(**request_data)
			
			reader.save()
			
			return HttpResponse(json.dumps(reader.to_dict(), cls=DjangoJSONEncoder), status=201,
			                    content_type=APPLICATION_JSON)
		
		
		except Exception as ex:
			print(ex)
			logger.error("Exception Occurred", str(ex))
			data = {
				"message": "Invalid data for Signup",
				"status": 400
			}
			return HttpResponse(json.dumps(data), status=400, content_type=APPLICATION_JSON)
