from django.core.paginator import Paginator
from injector import inject

from ....utils.exceptions import NotFoundException, ValidationException
from ..repositories import BlogRepository
from ..serializers import (
    BlogCreateRequestSerializer,
    BlogResponseSerializer,
    BlogUpdateRequestSerializer,
)


class BlogService:
    @inject
    def __init__(self, blog_repository: BlogRepository):
        self.blog_repository = blog_repository

    def get_blogs(self, request):
        page = request.query_params.get("page", 1)
        limit = request.query_params.get("limit", 10)
        blogs = self.blog_repository.find_all() or []

        paginator = Paginator(blogs, limit)
        page_obj = paginator.get_page(page)

        return (
            BlogResponseSerializer(page_obj, many=True).data,
            paginator.count,
            paginator.num_pages,
            page_obj.number,
        )

    def __find_blog_by_id(self, blog_id):
        try:
            blog = self.blog_repository.find_by_id(blog_id)
            return blog
        except Exception:
            raise NotFoundException("Blog not found.")

    def get_blog(self, blog_id):
        blog = self.__find_blog_by_id(blog_id)
        return BlogResponseSerializer(blog).data

    def create_blog(self, blog_data, user_data):
        user = user_data
        request_data = blog_data.copy()
        request_data["author"] = user.id
        serializer = BlogCreateRequestSerializer(data=request_data)

        if serializer.is_valid():
            blog = serializer.save()
            return BlogResponseSerializer(blog).data
        else:
            raise ValidationException(detail=serializer.errors)

    def update_blog(self, blog_id, blog_data, partial=False):
        blog = self.__find_blog_by_id(blog_id)
        serializer = BlogUpdateRequestSerializer(blog, data=blog_data, partial=partial)

        if serializer.is_valid():
            blog = serializer.save()
            return BlogResponseSerializer(blog).data
        else:
            raise ValidationException(detail=serializer.errors)

    def delete_blog(self, blog_id):
        blog = self.__find_blog_by_id(blog_id)
        blog.delete()
