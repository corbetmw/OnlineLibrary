from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from app.book_contoller import *
from app.catalog import *


def signup(request):
    """
    This view handles user creation. Nice!
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

def login_view(request):
    """
    Logs the use in
    :param request:
    :return: either a redirect or a failure message
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect('/')
    else:
        return HttpResponse('Your login failed')

def logout_view(request):
    logout(request);
    return render(request,'app/base.html')

def index(request):
    """
    The index  view
    :param request:
    :return:
    """
    return render(request, 'app/landing.html')

@login_required
def books(request):
    """
    The books list view. This is the list of all books that have been checked out by users.
    :param request:
    :return:
    """
    books = get_all_books()
    context = {'books': books}
    return render(request, 'app/books.html', context)

@login_required
def book(request, book_id):
    """
    The single book detail view
    :param request:
    :param book_id:
    :return:
    """
    book = get_book_by_id(book_id)
    context = {'book':book}
    return render(request, 'app/book.html', context)

@login_required
def catalog(request, searchString = 'the sun also rises'):
    """
    The catalog view. It pulls in the data from the api and makes a table
    :param request:
    :param searchString:
    :return:
    """
    catalogBooks = searchCatalog(searchString)
    return render(request, 'app/catalog.html', {'catalogBooks': catalogBooks})

def my_books_view(request):
    """
    The mybooks view. It pulls in the data from the data base and
    displays it ina table
    :param request: the HTTP request
    :return:
    """
    myBooks = get_user_books_by_user(request.user.id)
    context = {'myBooks':myBooks}
    return render(request, 'app/myBooks.html', context)


def checkout_confirm_view(request):
    """
    Gets the parameters from the url and renders the checkout template
    :param request: the request passed by the URL
    :param title: the title passed by the URL
    :param author: the author passed by the URL
    :param subject: the subject passed by the URL
    :param publisher: the publisher passed by the URL
    :return:the rendered checkout page
    """
    title = request.GET['title']
    author = request.GET['author']
    subject = request.GET['subject']
    publisher = request.GET['publisher']

    catalogBook = CatatlogBook(title,author,subject,publisher)
    context = {'catalogBook':catalogBook}
    return render(request, 'app/checkout.html',context)

def checkout(request):
    """
    Processes the request and checks ou tthe book for the
    user in the requst
    :param request:
    :return:
    """
    user_id = request.user.id
    # populate our values
    title = request.POST['title']
    author = request.POST['author']
    subject = request.POST['subject']
    publisher = request.POST['publisher']
    # Generate the book
    book = Book(title,author,subject,publisher)
    # Check it out for the current user
    check_out_book(user_id,book)
    return  redirect('/mybooks/')

@require_POST
@csrf_exempt
def get_all_books_as_json_view(request):
    """ POST only API Endpoint to get Books as JSON. """
    return HttpResponse(get_all_books_in_json(), content_type = 'application/json')

@require_POST
@csrf_exempt
def get_all_users_as_json_view(request):
    """ POST only API Endpoint to get Books as JSON. """
    return HttpResponse(get_all_users_in_json(), content_type = 'application/json')

@require_POST
@csrf_exempt
def get_all_userbooks_as_json_view(request):
    """ POST only API Endpoint to get Books as JSON. """
    return HttpResponse(get_all_userbooks_in_json(), content_type = 'application/json')