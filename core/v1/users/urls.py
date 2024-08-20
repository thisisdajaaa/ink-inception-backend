from django.urls import path

from core.utils.helpers import routers

from .views import RoleView, UserView

router = routers.OptionalSlashRouter()

app_name = "users"

urlpatterns = [
    # UserView
    path("", UserView.as_view(), name="user-list-create"),
    path("users/<int:user_id>/", UserView.as_view(), name="user-detail-update-delete"),
    # RoleView
    path("", RoleView.as_view(), name="role-list-create"),
    path("roles/<int:role_id>/", RoleView.as_view(), name="role-detail-update-delete"),
]
