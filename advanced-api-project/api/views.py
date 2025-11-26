from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books (READ-ONLY for everyone)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view


# Retrieve a single book by ID (READ-ONLY for everyone)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'


# Create a new book (AUTHENTICATED ONLY)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Update an existing book (AUTHENTICATED ONLY)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


# Delete a book (AUTHENTICATED ONLY)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
