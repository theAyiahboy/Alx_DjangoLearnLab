from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required("bookshelf.can_create")
def create_book(request):
    return render(request, "create_book.html")

@permission_required("bookshelf.can_delete")
def delete_book(request, book_id):
    return redirect("home")
