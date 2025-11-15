from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied
from .models import Book, Library, UserProfile
from bookshelf.forms import CustomUserCreationForm


# ---------------------------
# Helper decorator for role + permission checks
# ---------------------------
def role_permission_required(roles=[], perm=None):
    """
    Decorator to check both user role and permission.
    Usage: @role_permission_required(roles=['Admin', 'Editor'], perm='relationship_app.can_add_book')
    """
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not hasattr(request.user, 'userprofile'):
                raise PermissionDenied("User has no profile.")
            
            if request.user.userprofile.role not in roles:
                raise PermissionDenied("You do not have the required role.")
            
            if perm and not request.user.has_perm(perm):
                raise PermissionDenied("You do not have the required permission.")
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

# ---------------------------
# Book Views
# ---------------------------
def list_books(request):
    """View to list all books."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

@role_permission_required(roles=['Admin', 'Editor'], perm='relationship_app.can_add_book')
def add_book(request):
    """Add a new book (Admins and Editors only)."""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@role_permission_required(roles=['Admin', 'Editor'], perm='relationship_app.can_change_book')
def edit_book(request, pk):
    """Edit a book (Admins and Editors only)."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@role_permission_required(roles=['Admin'], perm='relationship_app.can_delete_book')
def delete_book(request, pk):
    """Delete a book (Admins only)."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

# ---------------------------
# Library Views
# ---------------------------
class LibraryDetailView(DetailView):
    """Class-based view for Library detail page."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# ---------------------------
# Role-based dashboard views
# ---------------------------
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# ---------------------------
# User Registration
# ---------------------------
def register_view(request):
    """Register a new user with role selection."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            role = form.cleaned_data['role']
            user.save()
            # Create the UserProfile with selected role
            
            login(request, user)
            return redirect('list_books')
    else:
        form = CustomUserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
