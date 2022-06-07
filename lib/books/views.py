from django.shortcuts import render

from .forms import Genres, Authors


# Добовление жанра

def add_genres(request):
    formGenre = Genres()

    context = {
        'formGenre': formGenre,

    }
    if request.method == 'POST':

        form = Genres(request.POST)
        if form.is_valid():
            t = request.POST
            print(t)
            print(form.cleaned_data)
            categor = request.POST.get('genre')
            print(categor)
            form.save()
    return render(request, 'add_genres.html', context)

# Добовление автора

def add_authors(request):

    formAuthors = Authors()

    return render(request, 'add_authors.html')


def book(request):
    return render(request, 'book.html')


def add_book(request):
    return render(request, 'add_book.html')



