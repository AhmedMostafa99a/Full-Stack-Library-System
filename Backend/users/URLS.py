from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('bay/', views.show_books, name='bay'),
    path('add/omar/', views.book_create, name='omar'),
    path('bay/del/', views.person_delete, name='del'),
    path('update/<int:id>/', views.person_details, name='up'),
    path('update/<int:id>/set_new/', views.person_update, name='update'),
    path('search/', views.search_books, name='search'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('books/', views.user_books, name='books'),
    path('book/<int:id>/', views.book_details, name='book_details'),
    path('borrowed/', views.borrowed_books, name='borrowed'),
    path('borrow-book/', views.borrow_book, name='borrow_book'),
    path('return-book/', views.return_book, name='return_book'),
    path('profile/', views.profile, name='profile'),
]
