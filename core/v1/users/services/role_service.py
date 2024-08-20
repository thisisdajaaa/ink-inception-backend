from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from injector import inject

from ....utils.exceptions import NotFoundException, ValidationException
from ..repositories import RoleRepository
from ..serializers import (
    RoleCreateRequestSerializer,
    RoleResponseSerializer,
    RoleUpdateRequestSerializer,
)


class RoleService:
    @inject
    def __init__(self, role_repository: RoleRepository):
        self.role_repository = role_repository

    def get_roles(self, request):
        page = request.query_params.get("page", 1)
        limit = request.query_params.get("limit", 10)
        roles = self.role_repository.find_all() or []

        paginator = Paginator(roles, limit)
        page_obj = paginator.get_page(page)

        return (
            RoleResponseSerializer(page_obj, many=True).data,
            paginator.count,
            paginator.num_pages,
            page_obj.number,
        )

    def get_role(self, role_id):
        try:
            role = self.role_repository.get(pk=role_id)
        except ObjectDoesNotExist:
            raise NotFoundException("Role not found")

        return RoleResponseSerializer(role).data

    def create_role(self, role_data):
        serializer = RoleCreateRequestSerializer(data=role_data)

        if serializer.is_valid(raise_exception=True):
            role = serializer.save()
            return RoleResponseSerializer(role).data
        else:
            raise ValidationException(
                "Invalid role details provided!", errors=serializer.errors
            )

    def update_role(self, role_id, role_data):
        try:
            role = self.role_repository.get(pk=role_id)
        except ObjectDoesNotExist:
            raise NotFoundException("Role not found")
        serializer = RoleUpdateRequestSerializer(role, data=role_data)
        if serializer.is_valid(raise_exception=True):
            role = serializer.save()
            return RoleResponseSerializer(role).data

    def delete_role(self, role_id):
        try:
            role = self.role_repository.get(pk=role_id)
            role.delete()
        except ObjectDoesNotExist:
            raise NotFoundException("Role not found")
