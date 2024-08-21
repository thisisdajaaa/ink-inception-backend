from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.utils.helpers import routers

from .views import (
    UserLoginView,
    UserLogoutView,
    UserRegisterView,
)

router = routers.OptionalSlashRouter()

app_name = "authentication"

urlpatterns = [
    path("authentication/register", UserRegisterView.as_view(), name="register"),
    path("authentication/login", TokenObtainPairView.as_view(), name="login"),
    path("authentication/refresh", TokenRefreshView.as_view(), name="refresh"),
    path("authentication/logout", UserLogoutView.as_view(), name="logout"),
]
