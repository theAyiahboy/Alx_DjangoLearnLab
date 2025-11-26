from django.db import models
from datetime import datetime

"""
Author model:
- Represents a writer
- Has a name field only
"""


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


"""
Book model:
- title: name of the book
- publication_year: integer
- author: foreign key → one author can have many books
"""


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
