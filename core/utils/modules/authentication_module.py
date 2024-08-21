from injector import Module, provider, singleton

from ...v1.authentication.services import AuthService
from ...v1.users.repositories import UserRepository
from ...v1.users.services import UserService


class AuthenticationModule(Module):
    @provider
    @singleton
    def provide_authentication_service(
        self, user_repository: UserRepository, user_serivce: UserService
    ) -> AuthService:
        return AuthService(user_repository=user_repository, user_service=user_serivce)
