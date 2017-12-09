from django.urls import path
from . import views

app_name="app"

urlpatterns = [

    # List of all books checked out by all users: /books/
    path('', views.index, name='index'),
    path('books/',views.books, name='books'),
    path('books/<int:book_id>/', views.book, name='book'),
    path('catalog/search/<str:searchString>', views.catalog, name='catalog'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/checkout/', views.checkout_view, name='checkout_view'),
    path('createaccount/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('api/getallbooks', views.get_all_books_as_json_view, name='get_all_books_as_json_view'),
    path('api/getallusers', views.get_all_users_as_json_view, name='get_all_users_as_json_view'),
    path('api/getalluserbooks', views.get_all_userbooks_as_json_view, name='get_all_userbooks_as_json_view'),

]
