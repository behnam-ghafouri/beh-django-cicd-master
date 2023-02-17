from django.urls import path

from . import views
from . import calc
urlpatterns = [
    path('', views.index, name='index'),
    path('func1',calc.clc_)
]