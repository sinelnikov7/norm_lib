from django.urls import path

from .views import take_book, all_take

app_name = 'take_return_book'

urlpatterns = [
    path('take_book/', take_book, name='take_book'),
    path('all_take/', all_take, name='all_take'),
]
