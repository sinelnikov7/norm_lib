from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ActGiveOutForm, OrderEdit
from .models import ActGiveOut
from client.models import Client
from books.models import Book
import datetime
from django.db.models import Q
from django.shortcuts import get_object_or_404
import re


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
            # try:
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
            for n in books:
                boo = Book.objects.get(id=n)
                count = book.count_now
                boo.count_now -= 1
                boo.save()
            # except:
            #     print("чето не то")

        else:
            context = {
                'form': form
            }
            return render(request, 'take_book.html', context)
    return render(request, 'take_book.html', context)

@login_required
def all_take(request):
    all_take = ActGiveOut.objects.all()
    context = {
        'all_take': all_take,
    }
    # date1 = ActGiveOut.objects.get(id=10).today_date
    # date3 = ActGiveOut.objects.get(id=10).diff_date_minus()
    # a = ActGiveOut.objects.get(id=24)
    # a.today_date = '2022-06-20'
    # a.save()
    # date2 = datetime.date.today()
    # print(date1, 'Дата создания--------------------------------------------------')
    # print(date2, 'Сегодняшняя дата-----------------------------------------------')
    # print(date2-date2)

    return render(request, 'all_take.html', context)


def search_take(request):
    all_take = ActGiveOut.objects.all()
    context = {
        'all_take': all_take,
    }

    if request.method == "GET":
        firstName = request.GET.get('firstName')

        lastName = request.GET.get('lastName')

        try:
            client_id = Client.objects.get(name=firstName.title(), sur_name=lastName.title())

            all_take = ActGiveOut.objects.filter(Q(client_id=client_id.id))
            context = {
                'all_take': all_take,

            }
        except:

            context = {
                'not_found': 'Такие Имя и Фамилия не найдены',

            }

    return render(request, 'all_take.html', context)

@login_required
def order_edit(request, id):
    # order = get_object_or_404(ActGiveOut, id)

    order = ActGiveOut.objects.get(id=id)

    must = len(order.booksMustReturn.all())

    if request.method == "POST":
        # form = OrderEdit(request.POST, instance=order)
        orders = request.POST.getlist("booksMustReturn")
        refund = len(orders)
        if must == refund:
            price = 0
            for book in order.booksMustReturn.all():
                count_day = int(re.findall(r'\d', str(order.today_date - datetime.date.today()))[0])
                price += (book.price_for_day * count_day)
            order.status = f'Читатель вернул все книги, общая итоговая сумма составила {price} мегарублей'
            order.save()
            a = Client.objects.get(id=order.client_id)
            a.canGet = True
            a.save()
            for i in orders:
                order.booksMustReturn.remove(i)
                b = Book.objects.get(id=i)
                b.count_now += 1
                b.save()
                pass

        else:
            price = 0
            # те что пришли
            for i in orders:
                order.booksMustReturn.remove(i)
                b = Book.objects.get(id=i)
                b.count_now += 1
                b.save()
                count_day = int(re.findall(r'\d', str(order.today_date - datetime.date.today()))[0])
                price += (b.price_for_day * count_day)

            # те что остались
            elseBook = order.booksMustReturn.all()

            status = 'Читатель не вернул: '
            for i in elseBook:

                order.booksMustReturn.remove(i)
                b = Book.objects.get(id=i.id)
                b.count_now += 1
                b.save()
                price += b.price
                if i == elseBook[len(elseBook) - 1]:
                    status = f'{status} ' + f'{i}.'
                else:
                    status = f'{status} ' + f'{i},'

            status = f'{status} И итоговая сумма с учетом возмещения за не возвращенные книги составила - {price} мегарублей.'
            order.status = status
            order.save()
            a = Client.objects.get(id=order.client_id)
            a.canGet = True
            a.save()

    # form = OrderEdit(instance=order)

    context = {
        # 'form': form,
        'order': order,
    }
    return render(request, 'order_edit.html', context)
