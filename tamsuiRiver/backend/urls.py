from django.urls import path

from . import views

urlpatterns = [
    #path('/index.html', views.index),
    path('', views.index, name='index'),
]