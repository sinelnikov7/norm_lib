from django.urls import path

from .views import authorization

app_name = 'client'
urlpatterns =[
    path('', authorization, name='authorization')
]