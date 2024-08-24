from injector import Module

from .authentication_module import AuthenticationModule
from .blog_module import BlogModule
from .profile_module import ProfileModule
from .role_module import RoleModule
from .user_module import UserModule


class AppModule(Module):
    def configure(self, binder):
        binder.install(UserModule())
        binder.install(RoleModule())
        binder.install(ProfileModule())
        binder.install(AuthenticationModule())
        binder.install(BlogModule())
