from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def authors(request):
    return render(request, 'authors/authors.html')

# def book_signings(request):
#     return render(request, 'authors/book_signings.html')

from datetime import datetime
from .models import Author
from library.models import Book

def all_authors(request):
    return render(request, 'authors/all_authors.html')

def book_signings(request):
    return render(request, 'authors/book_signings.html')

def authors_books_view(request):
    #Get all authors (order alphabetically by last name)
    authors = Author.objects.order_by('last_name')
    
    #Filter: Authors born before 1995
    date = datetime(1995, 2, 23)
    old_authors = Author.objects.filter(birth_date__lt=date)
    
    #Exclude: Authors with no books published
    authors_with_books = Author.objects.exclude(book__isnull=True).distinct()
    
    #Get specific author by their first name and last name
    try:
        specific_author = Author.objects.get(first_name='Tobiloba', last_name='Akinleye')
    except Author.DoesNotExist:
        specific_author = None
        
    #Fetch all books and order them by publication date
    recent_books = Book.objects.order_by('-published_on')[:5] #Latest 5 books
    
    # Pass all the retrieved data to the template
    context = {
        'authors': authors,
        'old_authors': old_authors,
        'authors_with_books': authors_with_books,
        'specific_author': specific_author,
        'recent_books': recent_books,
    }
    return render(request, 'authors/authors_books.html', context)

