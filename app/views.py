from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from app.models import Book
from app.catalog import *


def index(request):
    return render(request, 'app/landing.html')

def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'app/books.html', context)

def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'app/book.html', {'book': book})

def catalog(request, searchString = 'the sun also rises'):
    catalogBooks = searchCatalog(searchString)
    return render(request, 'app/catalog.html', {'catalogBooks': catalogBooks})
