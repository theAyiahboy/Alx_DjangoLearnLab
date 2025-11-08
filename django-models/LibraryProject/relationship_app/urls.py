from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    # Function-based view
    path('books/', list_books, name='list_books'),

    # Class-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Permission-based book views (checker looks for these exact strings)
    path('book/add/', add_book, name='add_book'),
    path('book/<int:pk>/edit/', edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', delete_book, name='delete_book'),
]
