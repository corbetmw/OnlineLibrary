from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from app.models import Book
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
    books = Book.objects.all()
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
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'app/book.html', {'book': book})

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
