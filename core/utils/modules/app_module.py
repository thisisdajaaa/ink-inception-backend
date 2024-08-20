from injector import Module

from .user_module import UserModule


class AppModule(Module):
    def configure(self, binder):
        binder.install(UserModule())
