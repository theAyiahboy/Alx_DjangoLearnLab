# api/views.py
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Existing ListAPIView
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for CRUD
class BookViewSet(viewsets.ModelViewSet):
    """
    Handles all CRUD operations:
    - GET /books_all/       -> list all books
    - GET /books_all/<id>/  -> retrieve one book
    - POST /books_all/      -> create a book
    - PUT /books_all/<id>/  -> update a book
    - DELETE /books_all/<id>/ -> delete a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
