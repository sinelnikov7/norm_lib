from django.urls import path

from .views import book, add_book, add_genres, add_authors

app_name = 'book'
urlpatterns = [

    path('', book, name='book'),
    path('add_book/', add_book, name='add_book'),
    path('add_genres/', add_genres, name='add_genres'),
    path('add_authors/', add_authors, name='add_authors'),
]