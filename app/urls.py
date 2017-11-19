from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from app.models import Book, UserBook
# from forms import RestaurantForm, DishForm
# from views import RestaurantCreate, DishCreate, RestaurantDetail

urlpatterns = [

# List of all books checked out by all users: /books/
    url(r'\^\$',
        ListView.as_view(
        	queryset=Book.objects.all(),
        	context_object_name='book_list',
        	template_name='books/book_list.html'),
        name='book_list'),
    # Book details from /books/, ex: /books/1
    url(r'\^books/(?P<pkr>\d+)/\$',
        DetailView.as_view(
            model=Book,
            template_name='books/book_detail.html'),
        name='dish_detail')

]