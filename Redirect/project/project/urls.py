"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.myredirect,name='myredirect'),
    path('myredirect1/',views.myredirect1,name='myredirect1'),
    path('home/',views.home,name='home'),
    path('myredirect2/',views.myredirect2,name='myredirect2'),
    path('home1/',views.home,name='home1'),
    path('myredirect3/',views.myredirect3,name='myredirect3'),
    path('home3/',views.home3,name='home3'),
]
