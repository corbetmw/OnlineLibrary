import json
import requests

class CatatlogBook(object):
    title = ''
    author = ''
    subject = ''
    publisher = ''

    def __init__(self, title, author, subject, publisher):
        self.title = title
        self.author = author
        self.subject = subject
        self.publisher = publisher

def searchCatalog(searchString):
    """ Searches the book api with a search string  """
    searchString.replace(" ", "+")
    response = requests.get("http://openlibrary.org/search.json?q=" + searchString)
    bookJson = response.json()
    catalogBooks = []

    for book in bookJson['docs']:
        try:
            currentTitle = book['title']
        except:
            currentTitle = ''
        try:
            currentAuthor = book['author_name'][0]
        except:
            currentAuthor = ''
        try:
            currentSubject = book['subject'][0]
        except:
            currentSubject = ''
        try:
            currentPublisher = book['publisher'][0]
        except:
            currentPublisher = ''

        currentCatalogBook = CatatlogBook(currentTitle,currentAuthor,currentSubject,currentPublisher)
        catalogBooks.append(currentCatalogBook)

    return catalogBooks
