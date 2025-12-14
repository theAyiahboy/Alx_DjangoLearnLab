from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Accounts API
    path("api/accounts/", include("accounts.urls")),

    # Posts API (feed, like, unlike)
    path("api/", include("posts.urls")),
]
