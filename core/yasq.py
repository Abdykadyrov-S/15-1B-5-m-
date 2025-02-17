# drf_yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include


schema_view = get_schema_view(
   openapi.Info(
      title="MerrigardenAPI",
      default_version='v1',
      description="Descriptions",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="abdykadyrovsyimyk0708@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns_yasq = [
    # drf_yasg
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='api_swagger'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]