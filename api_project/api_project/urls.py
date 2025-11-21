# api_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # Token endpoint

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include your API app URLs
    path('api/', include('api.urls')),

    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
