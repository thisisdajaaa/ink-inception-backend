from django.contrib.auth import authenticate
from injector import inject
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from ....utils.exceptions import ValidationException
from ...users.repositories import UserRepository
from ...users.serializers import UserResponseSerializer
from ...users.services import UserService
from ..serializers import (
    TokenSerializer,
    UserLoginSerializer,
    UserRegistrationSerializer,
)


class AuthService:
    @inject
    def __init__(self, user_repository: UserRepository, user_service: UserService):
        self.user_repository = user_repository
        self.user_service = user_service

    def register_user(self, user_data):
        serializer = UserRegistrationSerializer(data=user_data)
        if serializer.is_valid():
            user = self.user_service.create_user(serializer.validated_data)
            return UserResponseSerializer(user).data
        else:
            raise ValidationException(detail=serializer.errors)

    def login_user(self, credentials):
        serializer = UserLoginSerializer(data=credentials)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )
            if user:
                refresh = RefreshToken.for_user(user)
                return TokenSerializer(
                    {"refresh": str(refresh), "access": str(refresh.access_token)}
                ).data
            else:
                raise ValidationException(
                    detail={"non_field_errors": ["Invalid username or password."]}
                )
        else:
            raise ValidationException(detail=serializer.errors)

    def logout_user(self, refresh_token):
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return {"detail": "Successfully logged out."}
        except (TokenError, InvalidToken) as e:
            raise ValidationException(detail={"non_field_errors": [str(e)]})
