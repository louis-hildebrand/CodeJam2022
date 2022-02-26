from django.urls import path

from . import views

urlpatterns = [
    path('', views.find_path, name='find_path'),
    path('test', views.test, name='test'),
]
