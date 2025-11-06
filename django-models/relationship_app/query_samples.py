from relationship_app.models import Author, Book, Library, Librarian


# ---------------------------------------------------------------
# 1. Query all books by a specific author
# ---------------------------------------------------------------
def books_by_author(author_name):
    """
    Returns all books written by an author with the given name.
    Handles multiple authors with the same name safely.
    """
    authors = Author.objects.filter(name=author_name)
    if not authors.exists():
        return []
    return Book.objects.filter(author__in=authors)


# ---------------------------------------------------------------
# 2. List all books in a specific library
# ---------------------------------------------------------------
def books_in_library(library_name):
    """
    Returns all books available in a library with the given name.
    Handles duplicate library names safely.
    """
    libraries = Library.objects.filter(name=library_name)
    if not libraries.exists():
        return []
    return libraries.first().books.all()


# ---------------------------------------------------------------
# 3. Retrieve the librarian for a library
# ---------------------------------------------------------------
def librarian_for_library(library_name):
    """
    Returns the Librarian assigned to a library with the given name.
    Returns None if the library or librarian does not exist.
    """
    library = Library.objects.filter(name=library_name).first()
    return getattr(library, 'librarian', None) if library else None
