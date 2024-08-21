from injector import Module

from .profile_module import ProfileModule
from .role_module import RoleModule
from .user_module import UserModule


class AppModule(Module):
    def configure(self, binder):
        binder.install(UserModule())
        binder.install(RoleModule())
        binder.install(ProfileModule())
