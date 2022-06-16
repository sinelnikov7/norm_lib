from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import Genre, Author, AddBook
from .models import Genres, Authors, FotosAuthor, Book, FotoBook


# Добовление жанра
@login_required
def add_genres(request):
    form = Genre()
    allGenres = Genres.objects.all()

    context = {
        'form': form,
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
        else:
            allGenres = Genres.objects.all()
            context = {
                'form': form,
                'allGenres': allGenres,
            }
            print(form.errors)
            return render(request, 'add_genres.html', context)
    return render(request, 'add_genres.html', context)


# Добовление автора
@login_required
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

@login_required
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
    books = Book.objects.all()
    genres = Genres.objects.all()
    authors = Authors.objects.all()
    fotoAutors = FotosAuthor.objects.all()
    fotoBooks = FotoBook.objects.all()

    context = {
        'books': books,
        'genres': genres,
        'authors': authors,
        'fotoAutors': fotoAutors,
        'fotoBooks': fotoBooks,
    }
    # a = Genres.objects.get(pk=8)
    # gen = Book.objects.filter(genres__id=8)
    # gen = Genres.objects.filter(book__id=6)
    # gen = genres.filter(book__id=6)
    # print(gen)
    # print(a.book_set.all())
    # fot = Authors.objects.get(id=2)
    # print(fot.authors.all())

    return render(request, 'book.html', context)


def book_detail(request, id):
    book = Book.objects.get(id=id)
    print(book)
    context = {
        'book': book,
    }

    return render(request, 'book_detail.html', context)
