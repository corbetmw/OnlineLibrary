"""
This module controls all book transactions including the creation of new books and the
checking of them out to users.
"""

from .models import *

def get_user_books_by_user(user_id):
    """
    Given a user ID, get all the books
    they have checkd out
    :param user_id:
    :return: List of Book objects
    """
