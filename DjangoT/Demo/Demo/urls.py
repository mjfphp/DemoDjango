"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from TestApp.views import Index,Home,Sd,Students,Register,Crypt
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
    path('home',Home,name='home'),
    path('register',Register,name='register'),
    path('students',Students,name='students'),
    path('des1',Crypt,name='des1'),
    url(r'sd/(?P<sid>[0-9]+)',Sd,name='sd')
]
