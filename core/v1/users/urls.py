from django.urls import path

from core.utils.helpers import routers

from .views import UserView

router = routers.OptionalSlashRouter()

app_name = "users"

urlpatterns = [
    path("", UserView.as_view(), name="user-list-create"),
    path("users/<int:user_id>/", UserView.as_view(), name="user-detail-update-delete"),
]
