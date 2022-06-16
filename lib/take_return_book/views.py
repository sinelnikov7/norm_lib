from django.shortcuts import render, redirect

from .forms import ActGiveOut


def take_book(request):
    if request.method == 'POST':
        form = ActGiveOut(request.POST)
        if form.is_valid():
            return redirect('take_book.html')
    else:
        form = ActGiveOut()

    context = {
        'form': form
    }
    return render(request, 'take_book.html', context)

def return_book(request):
    return render(request, 'return_book.html')



