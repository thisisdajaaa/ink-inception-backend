from injector import Injector
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ....utils.helpers.responses import CustomRenderer, formatPaginatedData
from ....utils.modules.app_module import AppModule
from ..services import BlogService

injector = Injector([AppModule()])


class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [CustomRenderer]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.blog_service = injector.get(BlogService)

    def get(self, request, blog_id=None):
        if blog_id:
            blog = self.blog_service.get_blog(blog_id)
            return Response(blog, status=status.HTTP_200_OK)
        else:
            details = self.blog_service.get_blogs(request)
            data = formatPaginatedData(details)
            return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        data = self.blog_service.create_blog(request.data, request.user)
        return Response(data, status=status.HTTP_201_CREATED)

    def patch(self, request, blog_id):
        data = self.blog_service.update_blog(blog_id, request.data, partial=True)
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, _, blog_id):
        self.blog_service.delete_blog(blog_id)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
