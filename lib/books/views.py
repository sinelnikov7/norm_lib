from django.shortcuts import render

from .forms import Genre, Author, AddBook
from .models import Genres, Authors, FotosAuthor, Book, FotoBook


# Добовление жанра

def add_genres(request):
    formGenre = Genre()
    allGenres = Genres.objects.all()

    context = {
        'formGenre': formGenre,
        'allGenres': allGenres,
    }
    if request.method == 'POST':

        form = Genre(request.POST)
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
    formAuthors = Author()
    author = Authors.objects.all()
    foto = FotosAuthor.objects.all()
    context = {
        'formAuthors': formAuthors,
        'author': author,
        'foto': foto,
    }
    if request.method == 'POST':
        images = request.FILES.getlist('foto')
        print(images)
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        # a - переменная для записи авторов
        a = Authors()
        a.lastName = lastName
        a.firstName = firstName
        a.save()
        pk = a.pk
        for i in images:
            authors = Authors.objects.get(pk=pk)
            FotosAuthor.objects.create(foto=i, authors=authors)

        print(firstName, lastName, 'из формы')

    return render(request, 'add_authors.html', context)


def add_book(request):
    form = AddBook()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = AddBook(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            a = Book()
            a.name_r = request.POST.get('name_r')
            a.name_o = request.POST.get('name_o')
            a.price = request.POST.get('price')
            a.count = request.POST.get('count')
            a.price_for_day = request.POST.get('price_for_day')
            a.year_of_made = request.POST.get('year_of_made')
            a.count_of_pages = request.POST.get('count_of_pages')
            genres = request.POST.getlist('genres')
            print("genres = ", genres)
            authors = request.POST.getlist('authors')
            print("authors = ", authors)
            images = request.FILES.getlist('foto')
            a.save()
            pk = a.pk
            for i in genres:
                print(i)
                print(Genres.objects.all())
                genre = Genres.objects.get(id=i)
                a.genres.add(genre.id)
            for n in authors:
                author = Authors.objects.get(id=n)
                a.authors.add(author.id)

            for image in images:
                book = Book.objects.get(pk=pk)
                FotoBook.objects.create(foto=image, book=book)


            print(form.cleaned_data)
        else:
            print('Не зашло')
            pass
    return render(request, 'add_book.html', context)


def book(request):
    return render(request, 'book.html')
