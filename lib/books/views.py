from django.shortcuts import render


def book(request):
    return render(request, 'book.html')

def add_book(request):
    return render(request, 'add_book.html')

def add_genres(request):
    return render(request, 'add_genres.html')

def add_authors(request):
    return render(request, 'add_authors.html')
