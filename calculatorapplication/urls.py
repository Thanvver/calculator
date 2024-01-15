"""
URL configuration for calculatorapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from operations.views import HelloWorldView
from operations.views import GoodMorningView
from operations.views import GoodEveningView
from operations.views import GoodAfternoonView
from operations.views import GoodNightView
from operations.views import Addition
from operations.views import Subtraction
from operations.views import Division
from operations.views import Product
from operations.views import Cube
from operations.views import PrimeNumber
from operations.views import LeapYear
from operations.views import LongestWordView
from operations.views import BracketView
from operations.views import MostFrequentWord
from operations.views import LoanView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/",HelloWorldView.as_view()),
    path("morning/",GoodMorningView.as_view()),
    path("evening/",GoodEveningView.as_view()),
    path("afternoon/",GoodAfternoonView.as_view()),
    path("night/",GoodNightView.as_view()),
    path("addition/",Addition.as_view()),
    path("subtraction/",Subtraction.as_view()),
    path("division/",Division.as_view()),
    path("product/",Product.as_view()),
    path("cube/",Cube.as_view()),
    path("prime/",PrimeNumber.as_view()),
    path("leapyear/",LeapYear.as_view()),
    path("longestword/",LongestWordView.as_view()),
    path("brackets/",BracketView.as_view()),
    path("frequent/",MostFrequentWord.as_view()),
    path("emi/",LoanView.as_view()),
    

    


]
