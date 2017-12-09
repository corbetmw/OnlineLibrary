"""
This module controls all book transactions including the creation of new books and the
checking of them out to users.
"""
from django.core import serializers
from django.shortcuts import get_object_or_404

from .models import *

def get_user_books_by_user(user_id):
    """
    Given a user ID, get all the books
    they have checkd out
    :param user_id:
    :return: List of Book objects
    """
    books = Book.objects.filter(userbook__user_id=user_id)
    return books

def get_user_books_by_book(book_id):
    """
    Given the book id, tell me all the
    users that have checked it out
    :param book_id:
    :return: list of users
    """
    users = User.objects.filter(userbook__book_id=book_id)
    return users

def get_book_by_id(book_id):
    """
    Given a single bookID, find the corresponding book
    in the database
    :param book_id:
    :return: Book
    """
    book = get_object_or_404(Book, pk=book_id)
    return book

def get_all_books():
    """
    Gets all books from the database
    :return: List of books
    """
    books = Book.objects.all()
    return books

def create_book(book):
    """
    Creates a book in the database given a populated book object
    :param book:
    :return: the id of the book just created
    """
    newBook = Book.objects.create(title=book.title,author=book.author,subject=book.subject,publisher=book.publisher)
    return newBook.id

def update_book(book):
    """
    Updates a given book
    :param book:
    :return:
    """
    Book.objects.filter(pk=book.id).update(title=book.title,
                                           author=book.author,
                                           subject=book.subject,
                                           publisher=book.publisher)


def delete_book(book_id):
    """
    Deletes a book from the DB
    :param book_id:
    :return:
    """
    Book.objects.filter(pk=book_id).delete()

def check_out_book(user_id,book):
    """
    Checks a book out by creating a
    record int he UserBooks table
    :param user_id:
    :param book:
    :return: the id of the UserBook justcreated
    """
    book_id = create_book(book)
    userbook_id = UserBook.objects.create(user_id,book_id)
    return userbook_id

def get_all_books_in_json():
    """
    Gets all books and converts the data into JSON
    :return: serialized Books
    """
    books = Book.objects.all()
    return serializers.serialize('json', books)

def get_all_users_in_json():
    """
    Gets all users in JSON
    :return: serialized USer json
    """
    users = User.objects.all()
    return serializers.serialize('json', users)

def get_all_userbooks_in_json():
    """
    Gets all userbooks in JSON
    :return: serialized USerbook json
    """
    userbooks = UserBook.objects.all()
    return serializers.serialize('json', userbooks)

def update_user(user):
    """
    Updates a given user
    :param book:
    :return:
    """
    User.objects.filter(pk=user.id).update(user)

