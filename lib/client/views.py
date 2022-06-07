from django.shortcuts import render
from .forms import UserForm

def authorization(request):
    form = UserForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context ={
                'form':form

            }
            return render(request, 'authorization.html', context)

    return render(request, 'authorization.html', context)


# Create your views here.
