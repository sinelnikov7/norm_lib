from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import main

app_name = 'main'
urlpatterns =[
    path('', main, name='main')
]