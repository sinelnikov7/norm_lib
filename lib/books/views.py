from django.shortcuts import render


def book(request):
    return render(request, book, 'book.html')

# Create your views here.
