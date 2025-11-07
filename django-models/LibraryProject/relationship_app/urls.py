# relationship_app/urls.py
import importlib
try:
    django_urls = importlib.import_module('django.urls')
    path = django_urls.path
    include = django_urls.include
except Exception:  # ImportError or missing Django in the environment (editor/linter)
    # Provide a small fallback to avoid editor/linter import errors when Django isn't installed.
    def path(route, view, name=None):
        return (route, view, name)
    def include(arg):
        return arg

# from . import views
from . import views

# Try to import django.contrib.admin via importlib to avoid linter errors when Django isn't installed.
try:
    django_admin = importlib.import_module('django.contrib.admin')
    admin = django_admin
except Exception:
    # Provide a small admin stub so editor/linter won't complain and urlpatterns can still be inspected.
    class _AdminSiteStub:
        urls = 'admin/'

    class _AdminStub:
        site = _AdminSiteStub()

    admin = _AdminStub()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  
]
