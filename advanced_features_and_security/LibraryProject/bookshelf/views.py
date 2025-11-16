from .forms import ExampleForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .models import Book, Library
from .forms import BookForm

# -----------------------------
# Utility functions for role checks
# -----------------------------
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# -----------------------------
# Role-Based Dashboard Views
# -----------------------------
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'bookshelf/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'bookshelf/member_view.html')

# -----------------------------
# Library Detail View
# -----------------------------
@login_required
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'bookshelf/library_detail.html', {'library': library})

# -----------------------------
# Book CRUD Views
# -----------------------------

# List all books
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

# Create a new book
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})

# Update an existing book
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})

# Delete a book
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_delete.html', {'book': book})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
