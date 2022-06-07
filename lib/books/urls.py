from django.urls import path

from .views import book

app_name = 'book'
urlpatterns = [

    path('', book, name='book')
]
