from django.core.mail import message
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Genres(models.Model):
    genre = models.CharField(max_length=50, verbose_name='Жанр')

    def __str__(self):
        return self.genre


class Authors(models.Model):
    firstName = models.CharField(max_length=50, verbose_name='Имя')
    lastName = models.CharField(max_length=50, verbose_name='Фамилия')

    def __str__(self):
        return self.genre

class FotosAuthor(models.Model):
    foto = models.ImageField(upload_to='authors')
    authors = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name='authors')


class Book(models.Model):
    name_r = models.CharField(max_length=50, verbose_name='Название на русском')
    name_o = models.CharField(max_length=50, verbose_name='Название на языке оригинала', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.IntegerField(default=1, validators=[
        MinValueValidator(0, message='Минимальное количество составляет 0'),
        MaxValueValidator(10, message='Максимальное количество составляет 10')
    ])
    price_for_day = models.DecimalField(max_digits=6, decimal_places=2)
    year_of_made = models.IntegerField(max_length=4, error_messages={'unique':"Год может состоять из 4 чисел"})
    date_of_register = models.DateField(auto_now_add=True)
    count_of_pages = models.IntegerField(default=1, validators=[
        MinValueValidator(1, message='Минимальное количество страниц должно составлять 1')])
    genres = models.ManyToManyField(Genres)
    authors = models.ManyToManyField(Authors)

class FotoBook(models.Model):
    foto = models.ImageField(upload_to='books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')

# Create your models here.
