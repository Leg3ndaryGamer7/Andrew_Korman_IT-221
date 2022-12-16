#!/usr/bin/env python
__author__ = "Arana Fireheart"

from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]


# pages/urls.py
from django.urls import path
from .views import homePageView
urlpatterns = [
    path("", homePageView, name="home"),
]