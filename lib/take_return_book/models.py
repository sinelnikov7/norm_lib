import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User
from client.models import Client
from django.db import models
from books.models import Book


# акт выдачи книги
class ActGiveOut(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Читатель')
    today_date = models.DateField(auto_now_add=True)
    count_of_day = models.IntegerField(verbose_name='Дней использования', validators=[
        MinValueValidator(1, message='Минимальное количество дней составляет 1'),
        MaxValueValidator(30, message='Максимальное количество составляет 30')
    ])
    expected_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Предварительная цена', default=0.0)
    books = models.ManyToManyField(Book, verbose_name='Книги')


    # def save(self, *args, **kwargs):
    #     if self.expected_price is None:
    #         self.expected_price = self. + datetime.timedelta(self.count_of_day)
    #     super(ActGiveOut, self).save(*args, **kwargs)

# акт возврата книги
# class ActReturn(models.Model):
#     actual_return_date = models.DateField()

