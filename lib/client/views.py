from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm

def authorization(request):
    form = UserForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if request.POST.get('password') == request.POST.get('password_again'):
                user = User.objects.create_user(username=request.POST.get('username'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),email=request.POST.get('email'),password=request.POST.get('password'))
                user.save()
            else:
                error = 'Пароль не совпадает'
                context = {
                    'form': form,
                    'error':error

                }
                return render(request, 'authorization.html', context)
        else:
            context ={
                'form':form
            }
            return render(request, 'authorization.html', context)

    return render(request, 'authorization.html', context)


# Create your views here.
