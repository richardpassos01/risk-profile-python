from jsonschema import validate
from django.http import JsonResponse
from risk_profile.shared.error import custom_error
from risk_profile.shared.error import codes
from http import HTTPStatus

class ErrorHandlerrMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_template_response(self,_,response):
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, custom_error.CustomError):
            return JsonResponse({
                'message': exception.message,
                'code': exception.code
            }, status=exception.status)
        
        else:
            return JsonResponse({
                'message': 'INTERNAL SERVER ERROR',
                'code': codes.GenericErrorCode.INTERNAL_SERVER_ERROR.value
            }, status=HTTPStatus.INTERNAL_SERVER_ERROR)
