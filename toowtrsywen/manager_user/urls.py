from django.urls import path

from . import views

app_name = 'man'
urlpatterns = [
    path('', views.index, name='index'),  
]