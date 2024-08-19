from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ....utils.helpers.responses import CustomRenderer
from ..services import UserService


class UserView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [CustomRenderer]

    def get(self, request, user_id=None):
        user_service = UserService()
        if user_id:
            user = user_service.get_user(user_id)
            return Response(user, status=status.HTTP_200_OK)
        else:
            users, total, num_pages, current_page = user_service.get_users(request)
            data = {
                "users": users,
                "pagination": {
                    "total": total,
                    "num_pages": num_pages,
                    "current_page": current_page,
                    "count": len(users),
                },
            }
            return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        user_service = UserService()
        data = user_service.create_user(request.data)
        return Response(data, status=status.HTTP_201_CREATED)

    def put(self, request, user_id):
        user_service = UserService()
        data = user_service.update_user(user_id, request.data)
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        user_service = UserService()
        user_service.delete_user(user_id)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
