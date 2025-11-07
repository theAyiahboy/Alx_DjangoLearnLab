# relationship_app/views.py
try:
    # Use importlib to avoid static-analysis errors when Django isn't installed
    import importlib, importlib.util
    if importlib.util.find_spec('django.http') is not None:
        HttpResponse = importlib.import_module('django.http').HttpResponse
    else:
        # Let the outer try/except handle the fallback definition below
        raise ImportError("django.http not available")
except Exception:
    # Minimal fallback HttpResponse for editor/static-analysis environments where Django isn't installed.
    class HttpResponse:
        def __init__(self, content='', content_type='text/plain', status=200):
            self.content = content
            self.status_code = status
            self._content_type = content_type

        def __str__(self):
            return str(self.content)

        # provide a content_type attribute similar to Django's HttpResponse
        @property
        def content_type(self):
            return getattr(self, '_content_type', 'text/plain')

# Try to import Django's render helper; if Django isn't installed (e.g. in an editor environment),
# provide a minimal fallback so linting/analysis won't fail.
try:
    # Use importlib to avoid static-analysis errors when Django isn't installed
    import importlib, importlib.util
    if importlib.util.find_spec('django.shortcuts') is not None:
        render = importlib.import_module('django.shortcuts').render
    else:
        # Let the outer try/except handle the fallback definition below
        raise ImportError("django.shortcuts not available")
except Exception:
    def render(request, template_name, context=None):
        """
        Minimal fallback render that returns plain text for simple debugging/editor use.
        This is NOT a replacement for Django's template rendering in production.
        """
        if context and isinstance(context, dict) and 'books' in context:
            lines = []
            for b in context['books']:
                author_name = getattr(getattr(b, 'author', None), 'name', 'Unknown')
                title = getattr(b, 'title', 'Untitled')
                lines.append(f"{title} — {author_name}")
            return HttpResponse("\n".join(lines), content_type="text/plain")
        return HttpResponse('', content_type="text/plain")

try:
    # Use importlib to avoid static-analysis errors when Django isn't installed
    import importlib, importlib.util
    if importlib.util.find_spec('django.views.generic') is not None:
        DetailView = importlib.import_module('django.views.generic').DetailView
    else:
        # Let the outer try/except handle the fallback definition below
        raise ImportError("django.views.generic not available")
except Exception:
    # Minimal fallback DetailView for editor/static-analysis environments where Django isn't installed.
    class DetailView:
        model = None
        template_name = None
        context_object_name = None
        queryset = None

        @classmethod
        def as_view(cls, **kwargs):
            def _view(request, *args, **kwargs):
                # Simple diagnostic response; in real Django this renders a template/context.
                return HttpResponse(f"DetailView for {getattr(cls, 'model', None)}", content_type="text/plain")
            return _view

from .models import Book, Library  # adjust if your models live elsewhere

def list_books(request):
    """
    Function-based view that lists all books (title & author).
    Renders HTML template if present, otherwise returns plain text.
    """
    books = Book.objects.select_related('author').all()

    # Prefer HTML template if available
    try:
        return render(request, 'relationship_app/list_books.html', {'books': books})
    except Exception:
        # Fallback: plain text list
        lines = [f"{b.title} — {b.author.name}" for b in books]
        return HttpResponse("\n".join(lines), content_type="text/plain")

class LibraryDetailView(DetailView):
    """
    Class-based view showing a single Library and the books in it.
    Expects a Library model with a related name `books` or a ManyToMany/Reverse FK
    that can be accessed through `library.books.all`.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    # If you want to prefetch books for performance:
    queryset = Library.objects.prefetch_related('books__author').all()

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Library Project homepage!")
