# Create a Model, View, and URL for the Bookshelf App

This guide helps you set up the `bookshelf` app inside the `LibraryProject` Django project.

---

## 1️⃣ Create the `Book` model

Open **bookshelf/models.py** and add:

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
