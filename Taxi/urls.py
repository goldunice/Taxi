from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Taxi loyihasi uchun API",
        default_version='v1',
        description="No description",
        contact=openapi.Contact(email="AkmaljonGold@gmail.com"),

    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('drivers/', include('drivers.urls')),
                  path('operators/', include('operators.urls')),
                  path('payments/', include('payments.urls')),
                  path('users/', include('users.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
