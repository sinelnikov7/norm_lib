from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ActGiveOutForm
from .models import ActGiveOut
from client.models import Client
from books.models import Book
import datetime


@login_required
def take_book(request):
    form = ActGiveOutForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = ActGiveOutForm(request.POST)
        if form.is_valid():
            order = ActGiveOut()
            order.client = Client.objects.get(id=request.POST.get('client'))
            order.count_of_day = request.POST.get('count_of_day')
            books = request.POST.getlist('booksGot')
            price_count = 0
            for i in books:
                book = Book.objects.get(id=i)
                price_count += book.price
            if len(books) >= 2 and len(books) < 4:
                price_count = float(price_count) * 0.1
            elif len(books) >= 4:
                price_count = float(price_count) * 0.15
            order.expected_price = price_count
            order.save()
            can_get = Client.objects.get(id=request.POST.get('client'))
            can_get.canGet = False
            can_get.save()
            for i in books:
                book = Book.objects.get(id=i)
                order.booksMustReturn.add(book.id)
                order.booksGot.add(book.id)

        else:
            context = {
                'form': form
            }
            return render(request, 'take_book.html', context)
    return render(request, 'take_book.html', context)


def all_take(request):
    all_take = ActGiveOut.objects.all()
    context = {
        'all_take': all_take,
    }
    # date1 = ActGiveOut.objects.get(id=10).today_date
    # date3 = ActGiveOut.objects.get(id=10).diff_date_minus()
    # a = ActGiveOut.objects.get(id=10)
    # a.today_date = '2022-06-15'
    # a.save()
    # date2 = datetime.date.today()
    # print(date1, 'Дата создания--------------------------------------------------')
    # print(date2, 'Сегодняшняя дата-----------------------------------------------')
    # print(date2-date2)

    return render(request, 'all_take.html', context)
