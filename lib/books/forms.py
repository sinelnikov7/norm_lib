from django import forms

# Форма для создания жанров
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelMultipleChoiceField

from .models import Genres, Authors


class Genre(forms.ModelForm):
    genre = forms.CharField(max_length=50, label='Жанр', error_messages={'unique':"Такой жанр уже добавлен"}, help_text='Введите имя жанра',
                            widget=forms.TextInput(attrs={'placeholder': 'Введите имя жанра'}))

    class Meta:
        model = Genres
        fields = '__all__'


class Author(forms.Form):
    firstName = forms.CharField(max_length=50, label='Имя')
    lastName = forms.CharField(max_length=50, label='Фамилия')
    foto = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Фотографии авторов')


class AddBook(forms.Form):
    name_r = forms.CharField(max_length=50, label='Название на русском')
    name_o = forms.CharField(max_length=50, label='Название на языке оригинала', required=False)
    price = forms.DecimalField(max_digits=6, decimal_places=2, label='Цена')
    count = forms.IntegerField(label='Кол-во доступных')
    price_for_day = forms.DecimalField(max_digits=6, decimal_places=2, label='Цена за день')
    year_of_made = forms.IntegerField(label='Год написания')
    # date_of_register = forms.DateField(auto_now_add=True)
    count_of_pages = forms.IntegerField(label='Страниц в книге')

    genres = ModelMultipleChoiceField(
        queryset=Genres.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Выберите жанры'
    )

    authors = ModelMultipleChoiceField(
        queryset=Authors.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Выберите авторов'
    )
    foto = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Фотографии книги')
