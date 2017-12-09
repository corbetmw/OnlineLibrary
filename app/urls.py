from django.urls import path
from django.views.generic import DetailView, ListView, UpdateView
from app.models import Book, UserBook
from . import views

app_name="app"

urlpatterns = [

    # List of all books checked out by all users: /books/
    path('', views.index, name='index'),
    path('books/',views.books, name='books'),
    path('books/<int:book_id>/', views.book, name='book'),
    path('catalog/<str:searchString>', views.catalog, name='catalog'),

]
