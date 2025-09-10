"""MyHome2 URL Configuration

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
from django.contrib import admin
from django.urls import path

from myapp import views

from myapp.views import MyView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('display/',views.display),
    path('date/',views.date),
    path('wish/',views.wish),
    path('dt/',views.dt),

    path('durga/',views.durga),
    path('movie/',views.movie),
    path('sport/',views.sport),
    path('politic/',views.politic),

    path('empdata/',views.empdata),
    path('stud/',views.stud),

    path('studentinputview/',views.studentinputview),
    path('studentinputview2/',views.studentinputview2),
    
    path('indexview23/',views.indexview23),
    path('addmovie/',views.addmovie),
    path('listmovie/',views.listmovie),

    path('countview/',views.countview),

    path('homeview1/',views.homeview1),
    path('datetimeview/',views.datetimeview),
    path('resultview/',views.resultview),



    path('name1/',views.name1),
    path('age1/',views.age1),
    path('gf1/',views.gf1),
    path('result1/',views.result1),

    path('indexform/',views.indexform),
    path('additem/',views.additem),
    path('displayitem/',views.displayitem),

    path('about/', MyView.as_view()),
   

    

    

]
