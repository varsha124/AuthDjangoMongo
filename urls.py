from django.urls import path

from . import views

urlpatterns = [
    path('', views.method1, name='index'),
]