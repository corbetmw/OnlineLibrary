from django.test import TestCase

# Create your tests here.
from .book_contoller import *

class BookTestCase(TestCase):

    def setUp(self):
        # First create a test user
        User.objects.create_user(username = "John", password="Password!", email="john@gmail.com")

        # Setup a UserBook for JOhn
        userBook = UserBook.objects.create(self.id,1)

    def get_self_test(self):
        return User.objects.get(username="John")

    #Get the books for john
    def get_books_by_user_test(self):
        return get_user_books_by_user(self.id)

    def get_users_by_book_test(book_id=1):
        return get_user_books_by_book(book_id)

    def test_get_user(self):
        """ Tests getting the test user from the database """
        test_user = self.get_test_user()

        # Verify we can get the test_user
        self.assertIsNotNone(test_user)

    def test_get_book_by_id(book_id=1):
        return get_book_by_id(book_id)

    def test_get_all_books(self):
        return get_all_books()

    def test_check_out_book(self):
        book = get_book_by_id(1);
        return check_out_book(self.id, book)

    def test_delete_book(self):
        book_id = 1
        delete_book(book_id)

    def test_update_book(self):
        book = get_book_by_id(1)
        book.subject = 'something changed'
        update_book(book);

    def test_update_user(self):
        update_user(self)

