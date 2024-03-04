"""
URL configuration for DÉJANGÓ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Notebook.views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('', index),
    path('megoldas', megoldas),
    path('megoldas/2van', w_2van),
    path('megoldas/3gyarto', w_3gyarto),
    path('megoldas/4teljes', w_4teljes),
    path('megoldas/5vasarlas', w_5vasarlas),
    path('megoldas/6nulla', w_6nulla),
    path('megoldas/7intel', w_7intel),
    path('feltoltes', feltoltes),
    path('feltoltes/fajl/<str:tabla>/kuld', feltoltes_fajl_kuld),
    path('feltoltes/fajl/<str:tabla>', feltoltes_fajl),

]
