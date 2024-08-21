"""
URL configuration for ink_inception project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Alerto API Documentation",
        default_version="v1",
        description="API Documentation for Alerto backend",
        terms_of_service="",
        contact=openapi.Contact(email="adannanthony@gmail.com"),
        license=openapi.License(name="MIU License"),
    ),
    public=True,
)


urlpatterns = [
    path(f"api/v{settings.API_VERSION}/", include("core.v1.users.urls")),
    path(f"api/v{settings.API_VERSION}/", include("core.v1.blogs.urls")),
    path(
        f"api/v{settings.API_VERSION}/",
        include("core.v1.authentication.urls"),
    ),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
