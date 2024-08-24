from typing import Type

from django.apps import apps
from injector import Module, provider, singleton

from ...v1.blogs.models import Blog
from ...v1.blogs.repositories import BlogRepository
from ...v1.blogs.services import BlogService


class BlogModule(Module):
    @provider
    @singleton
    def provide_blog_model(self) -> Type[Blog]:
        return apps.get_model("blogs", "Blog")

    @provider
    @singleton
    def provide_blog_repository(self, blog_model: Type[Blog]) -> BlogRepository:
        return BlogRepository(model=blog_model)

    @provider
    @singleton
    def provide_blog_service(self, blog_repository: BlogRepository) -> BlogService:
        return BlogService(blog_repository=blog_repository)
