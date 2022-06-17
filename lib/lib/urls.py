"""lib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('book/', include('books.urls')),
<<<<<<< HEAD
    path('autorized/', include('client.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', include('django.contrib.auth.urls')),
    path('accounts/logout/', include('django.contrib.auth.urls')),
=======
    path('autorized/', include('client.urls'))

>>>>>>> de5bba6c8cc742d5cbecf608100ef13ee72407d6
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)