from relationship_app.models import Author, Book, Library, Librarian


# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    #  Use .filter(author=author) as required by checker
    return Book.objects.filter(author=author)


# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    #  Explicitly query using filter/get
    return Librarian.objects.get(library=library)
