from django.urls import path

from . import views

app_name = 'ctq'
urlpatterns = [
    path('', views.index, name='index'),   
] 