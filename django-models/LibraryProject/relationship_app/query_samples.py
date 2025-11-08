from relationship_app.models import Author, Book, Library, Librarian

# --- Existing query functions ---
# 1. Query all books by a specific author
def books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

# --- New: populate sample data ---
def populate_sample_data():
    # Clear existing data (optional)
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create Authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")

    # Create Books
    book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="A Game of Thrones", author=author2)

    # Create Libraries
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="Community Library")

    # Add books to libraries
    library1.books.set([book1, book3])
    library2.books.set([book2])

    # Create Librarians
    Librarian.objects.create(name="Alice", library=library1)
    Librarian.objects.create(name="Bob", library=library2)

    print("Sample data populated successfully!\n")

# --- Optional: a demo runner ---
def run_demo():
    populate_sample_data()

    print("=== Books by Author ===")
    for book in books_by_author("J.K. Rowling"):
        print(f"- {book.title}")

    print("\n=== Books in Library ===")
    for book in books_in_library("Central Library"):
        print(f"- {book.title}")

    librarian = librarian_of_library("Community Library")
    print(f"\nLibrarian of Community Library: {librarian.name}")
