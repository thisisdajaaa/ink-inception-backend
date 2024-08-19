from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from ....utils.exceptions import NotFoundException, ValidationException
from ..repositories import UserRepository
from ..serializers import (
    UserCreateRequestSerializer,
    UserResponseSerializer,
    UserUpdateRequestSerializer,
)


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_users(self, request):
        page = request.query_params.get("page", 1)
        limit = request.query_params.get("limit", 10)
        users = self.user_repository.find_all() or []

        paginator = Paginator(users, limit)
        page_obj = paginator.get_page(page)

        return (
            UserResponseSerializer(page_obj, many=True).data,
            paginator.count,
            paginator.num_pages,
            page_obj.number,
        )

    def get_user(self, user_id):
        try:
            user = self.user_repository.get(pk=user_id)
        except ObjectDoesNotExist:
            raise NotFoundException("User not found")

        return UserResponseSerializer(user).data

    def create_user(self, user_data):
        serializer = UserCreateRequestSerializer(data=user_data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return UserResponseSerializer(user).data
        else:
            raise ValidationException(
                "Invalid user details provided!", errors=serializer.errors
            )

    def update_user(self, user_id, user_data):
        try:
            user = self.user_repository.get(pk=user_id)
        except ObjectDoesNotExist:
            raise NotFoundException("User not found")
        serializer = UserUpdateRequestSerializer(user, data=user_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return UserResponseSerializer(user).data

    def delete_user(self, user_id):
        try:
            user = self.user_repository.get(pk=user_id)
            user.delete()
        except ObjectDoesNotExist:
            raise NotFoundException("User not found")
