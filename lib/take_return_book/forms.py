from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import ActGiveOut
from client.models import Client
from books.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelMultipleChoiceField
from django import forms


class ActGiveOutForm(ModelForm):
    def clean_booksGot(self):
        booksGot = self.cleaned_data['booksGot']
        if len(booksGot) > 5:
            print("что-то не так")
            raise ValidationError('Вы не можете выбрать более 5 книг')
        return booksGot

    def clean_client(self):
        client = self.cleaned_data['client']
        print(client,'id-шка')
        can_get = Client.objects.get(id=client.id)
        if can_get.canGet == False:
            print('Что-то не так')
            raise ValidationError('У выбранного читателя уже есть книги')
        return client


    class Meta:
        model = ActGiveOut
        fields = ['client', 'count_of_day', 'booksGot']


class OrderEdit(ModelForm):
    # booksMustReturn = forms.CharField(widget=forms.CheckboxSelectMultiple)
    booksMustReturn = ModelMultipleChoiceField(
        queryset=Book.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Выберите жанры'
    )
    class Meta:
        model = ActGiveOut
        fields = ['booksMustReturn']
