from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls')),
    path('api/', include('warga.api_urls')),
    path('api/auth/token/', obtain_auth_token, name='api-token-auth'),

    # ✅ URL untuk Dokumentasi API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # Generate schema.yml
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # Redoc UI
]