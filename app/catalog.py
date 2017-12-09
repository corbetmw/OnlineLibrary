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
    bookJson = response.json()
    catalogBooks = []

    for book in bookJson['docs']:
        currentTitle = ''
        currentAuthor = ''
        currentSubject = ''
        currentPublisher = ''
        if book['title']:
            currentTitle = book['title']
        if book['author_name'][0]:
            currentAuthor = book['author_name'][0]
        if book['subject'][0]:
            currentAuthor = book['subject'][0]
        if book['publisher'][0]:
            currentAuthor = book['publisher'][0]
        currentCatalogBook = CatatlogBook(currentTitle,currentAuthor,currentSubject,currentPublisher)
        catalogBooks.append(currentCatalogBook)

    return catalogBooks
