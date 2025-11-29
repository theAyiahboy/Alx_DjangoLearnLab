from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    API view to retrieve list of all books.
    Supports filtering, searching, and ordering.
    Read-only access for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtering, Searching, Ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filter fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Search fields
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default order


class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book by ID.
    Read-only access for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book by ID.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book by ID.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
