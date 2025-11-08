from django.contrib import admin
from django.urls import path, include  # include allows app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # include app URLs
]
