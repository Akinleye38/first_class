from django.urls import path
from . import views

app_name = "authors"

urlpatterns = [
    path('', views.authors, name='authors'),
    path('book-signings/', views.book_signings, name='book_signings'),
    path('authors-and-books/', views.authors_books_view, name='authors_and_books'),
]
