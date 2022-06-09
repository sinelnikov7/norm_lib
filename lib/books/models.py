from django.core.mail import message
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

#Добовление жанров. Сюда будет ссылатся модель Book по связи ManyToManyField
class Genres(models.Model):
    genre = models.CharField(max_length=50, verbose_name='Жанр', unique=True, error_messages={'unique':"Такой жанр уже добавлен"})

    def __str__(self):
        return self.genre

#Добовление Авторов. Сюда будет ссылатся модель Book по связи ManyToManyField
class Authors(models.Model):
    firstName = models.CharField(max_length=50, verbose_name='Имя')
    lastName = models.CharField(max_length=50, verbose_name='Фамилия')

    def __str__(self):
        return self.lastName

#Фото авторов, где каждое фото будет ссылаться на Автора
class FotosAuthor(models.Model):
    foto = models.ImageField(upload_to='authors')
    authors = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name='authors')
    # def __str__(self):
    #     return self.authors

#Htubcnhfwbz rybub
class Book(models.Model):
    name_r = models.CharField(max_length=50, verbose_name='Название на русском')
    name_o = models.CharField(max_length=50, verbose_name='Название на языке оригинала', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.IntegerField(default=1, validators=[
        MinValueValidator(0, message='Минимальное количество составляет 0'),
        MaxValueValidator(10, message='Максимальное количество составляет 10')
    ])
    price_for_day = models.DecimalField(max_digits=6, decimal_places=2)
    year_of_made = models.IntegerField(max_length=4, error_messages={'maxLength':"Год может состоять из 4 чисел"})
    date_of_register = models.DateField(auto_now_add=True)
    count_of_pages = models.IntegerField(default=1, validators=[
        MinValueValidator(1, message='Минимальное количество страниц должно составлять 1')])
    genres = models.ManyToManyField(Genres)
    authors = models.ManyToManyField(Authors)


#Фото книги, где каждое фото будет ссылаться на Автора
class FotoBook(models.Model):
    foto = models.ImageField(upload_to='books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='fotobook')

# Create your models here.
