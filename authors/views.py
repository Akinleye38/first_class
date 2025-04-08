from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def authors(request):
    return render(request, 'authors/authors.html')

def book_signings(request):
    return render(request, 'authors/book_signings.html')

