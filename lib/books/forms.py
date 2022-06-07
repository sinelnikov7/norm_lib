from django import forms

#Форма для создания жанров
from .models import Genres


class Genres(forms.ModelForm):
    genre = forms.CharField(max_length=50,  label='Жанр')

    class Meta:
        model = Genres
        fields = '__all__'

class Authors(forms.Form):
    firstName = forms.CharField(max_length=50, label='Имя')
    lastName = forms.CharField(max_length=50, label='Фамилия')
    foto = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Фотографии авторов')