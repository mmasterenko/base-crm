import os

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class CORSMiddleware(MiddlewareMixin):
    """
    allow cross original requests
    """
    def process_response(self, request, response):
        origin = os.environ.get('ACCESS_CONTROL_ALLOW_ORIGIN')
        if not origin:
            origin = request.environ.get('HTTP_ORIGIN')
        if not origin:
            origin = settings.ACCESS_CONTROL_ALLOW_ORIGIN

        allow_headers = 'Origin, X-Requested-With, Content-Type, Accept, Set-Cookie, Cookie, X-CSRFToken'

        response['Access-Control-Allow-Origin'] = origin
        response['Access-Control-Allow-Headers'] = allow_headers
        response['Access-Control-Expose-Headers'] = allow_headers
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
