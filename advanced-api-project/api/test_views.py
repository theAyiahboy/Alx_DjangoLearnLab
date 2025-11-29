# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
        # --- Users ---
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass')

        # --- Author ---
        self.author = Author.objects.create(name="Test Author")

        # --- Book ---
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

        # --- API URLs ---
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book.id})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.id})

    # -------------------------------
    # READ / LIST / DETAIL
    # -------------------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    # -------------------------------
    # CREATE
    # -------------------------------
    def test_create_book_requires_authentication(self):
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    # -------------------------------
    # UPDATE
    # -------------------------------
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'Updated Book', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    # -------------------------------
    # DELETE
    # -------------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # -------------------------------
    # FILTERING
    # -------------------------------
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + '?title=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + '?author__name=Test Author')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url + '?publication_year=2020')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -------------------------------
    # SEARCH
    # -------------------------------
    def test_search_books_by_title(self):
        response = self.client.get(self.list_url + '?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_author(self):
        response = self.client.get(self.list_url + '?search=Author')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -------------------------------
    # ORDERING
    # -------------------------------
    def test_order_books_by_title(self):
        response = self.client.get(self.list_url + '?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
