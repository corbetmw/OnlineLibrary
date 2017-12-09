import json
import requests

class CatatlogBook(object):
    title = ''
    author = ''
    subject = ''
    publisher = ''

def searchCatalog(searchString):
    """ Searches the book api with a search string  """
    searchString.replace(" ", "+")
    response = requests.get("http://openlibrary.org/search.json?q=" + searchString)
    catalogBookData = response.json()
    catalogBooks = [];

    for title, author_name, subject, publisher in catalogBooks['docs'].items():
        currentCatalogBook = CatatlogBook(title,author_name,subject,publisher)
        catalogBookData.append(currentCatalogBook)