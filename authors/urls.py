from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors, name='authors'),
    path('book-signings/', views.book_signings, name='book_signings'),
]
