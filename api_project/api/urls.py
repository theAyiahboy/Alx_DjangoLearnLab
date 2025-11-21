# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # ListAPIView route
    path('books/', BookList.as_view(), name='book-list'),

    # Include all router URLs (CRUD)
    path('', include(router.urls)),
]
