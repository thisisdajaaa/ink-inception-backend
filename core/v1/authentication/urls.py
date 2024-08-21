from django.urls import path
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenRefreshView,
)

from core.utils.helpers import routers

from .views import CurrentUserView, UserLoginView, UserRegisterView

router = routers.OptionalSlashRouter()

app_name = "authentication"

urlpatterns = [
    path("authentication/register", UserRegisterView.as_view(), name="register"),
    path("authentication/login", UserLoginView.as_view(), name="login"),
    path("authentication/refresh", TokenRefreshView.as_view(), name="refresh"),
    path("authentication/logout", TokenBlacklistView.as_view(), name="logout"),
    path("authentication/current-user", CurrentUserView.as_view(), name="current-user"),
]
