from django.urls import path

from core.utils.helpers import routers

from .views import BlogView

router = routers.OptionalSlashRouter()

app_name = "blogs"

urlpatterns = [
    # BlogView
    path("blogs", BlogView.as_view(), name="blog-list-create"),
    path("blogs/<str:blog_id>", BlogView.as_view(), name="blog-detail-update-delete"),
]
