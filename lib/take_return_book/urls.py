from django.urls import path

from .views import take_book, return_book

app_name = 'take_return_book'

urlpatterns = [
    path('take_book/', take_book, name='take_book'),
    path('return_book/', return_book, name='return_book'),
]
