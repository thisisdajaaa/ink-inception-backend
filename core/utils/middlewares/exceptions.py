from rest_framework.response import Response

from ..exceptions import AlreadyExistsException, NotFoundException, ValidationException


class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except Exception as e:
            return self.process_exception(request, e)

    def process_exception(self, request, exception):
        if isinstance(exception, NotFoundException):
            return Response(
                {
                    "status": 404,
                    "data": {},
                    "pagination": {},
                    "success": False,
                    "error": {"message": str(exception)},
                },
                status=404,
            )
        elif isinstance(exception, AlreadyExistsException):
            return Response(
                {
                    "status": 409,
                    "data": {},
                    "pagination": {},
                    "success": False,
                    "error": {"message": str(exception)},
                },
                status=409,
            )
        elif isinstance(exception, ValidationException):
            return Response(
                {
                    "status": 400,
                    "data": {},
                    "pagination": {},
                    "success": False,
                    "error": {"message": str(exception), "details": exception.errors},
                },
                status=400,
            )
        else:
            return Response(
                {
                    "status": 500,
                    "data": {},
                    "pagination": {},
                    "success": False,
                    "error": {"message": "Internal server error."},
                },
                status=500,
            )
