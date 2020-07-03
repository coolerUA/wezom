from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from market.views.index import index
from rest_framework import routers
from market.views.category import CategoryViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Delivery API",
        default_version='v1',
        description=''' 
          Documentation `ReDoc` view can be found [here](/redoc).
      ''',
        contact=openapi.Contact(email="admin@sys-admin.com.ua"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('v1/', include([
        path('generic/', include(router.urls)),
        path('market/', include('market.urls'))
    ])),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += [
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
