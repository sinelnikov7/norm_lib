import datetime

from django.contrib.auth.models import User
from django.db import models

from books.models import Book

# акт выдачи книги
class ActGiveOut(models.Model):
    reader_info = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Информация о читателе')
    today_date = models.DateField(auto_now_add=True)
    return_due_date = models.DateField(verbose_name='Дата возврата')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Предварительная цена')
    book = models.ManyToManyField(Book, verbose_name='Книга')

    def save(self, *args, **kwargs):
        if self.return_due_date is None:
            self.return_due_date = self.today_date.date() + datetime.timedelta(days=30)
        super(ActGiveOut, self).save(*args, **kwargs)

# акт возврата книги
class ActReturn(models.Model):
    actual_return_date = models.DateField()

