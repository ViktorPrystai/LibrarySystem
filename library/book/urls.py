from django.urls import path
from .views import book_list, book_detail, add_book

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('books/add/', add_book, name='add_book'),
]