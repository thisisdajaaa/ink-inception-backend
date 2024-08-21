from injector import Injector
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ....utils.helpers.responses import CustomRenderer
from ....utils.modules.app_module import AppModule
from ..services import AuthService

injector = Injector([AppModule()])


class UserLogoutView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [CustomRenderer]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.auth_service = injector.get(AuthService)

    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response(
                {"detail": "Refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = self.auth_service.logout_user(refresh_token)
        return Response(data, status=status.HTTP_204_NO_CONTENT)
