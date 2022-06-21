from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ActGiveOutForm
from .models import ActGiveOut
from client.models import Client
from books.models import Book


@login_required
def take_book(request):
    form = ActGiveOutForm()
    context = {
        'form': form,
    }
    print(form)
    if request.method == 'POST':
        form = ActGiveOutForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            order = ActGiveOut()
            order.client = Client.objects.get(id=request.POST.get('client'))
            order.count_of_day = request.POST.get('count_of_day')
            books = request.POST.getlist('books')
            price_count = 0
            for i in books:
                book = Book.objects.get(id=i)
                price_count += book.price
            order.expected_price = price_count
            order.save()
            for i in books:
                book = Book.objects.get(id=i)
                order.books.add(book.id)
        else:
            context = {
                'form': form
            }
            return render(request, 'take_book.html', context)
    return render(request, 'take_book.html', context)


def return_book(request):
    return render(request, 'return_book.html')
