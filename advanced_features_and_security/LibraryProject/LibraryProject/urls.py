from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from relationship_app import views  # ✅ Import views to access register_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include all routes from the app
    path('relationship_app/', include('relationship_app.urls')),

    # ✅ Direct access to registration from the root
    path('register/', views.register_view, name='register'),

    # Redirect root ('/') to book list page
    path('', lambda request: redirect('list_books')),
]
