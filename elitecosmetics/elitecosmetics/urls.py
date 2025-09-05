from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from store.views import CategoryViewSet, ProductViewSet, OrderViewSet
from auth.views import RegisterView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# API Router
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

# Swagger schema with JWT Bearer Auth
schema_view = get_schema_view(
    openapi.Info(
        title="EliteCosmetics API",
        default_version='v1',
        description="API documentation for the EliteCosmetics eCommerce project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@elitecosmetics.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Swagger Security Definitions (Bearer token)
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema

# Optional: Add Bearer token globally
swagger_settings = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'JWT Authorization header using the Bearer scheme. Example: "Authorization: Bearer <token>"',
        }
    }
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth endpoints
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/me/', UserDetailView.as_view(), name='user_detail'),

    # Swagger UI at /api/
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # JSON/YAML schema
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),

    # ReDoc UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # API endpoints under /api/v1/
    path('api/v1/', include(router.urls)),
]
