from django.urls import path

from . import views

app_name = 'man'
urlpatterns = [
    path('', views.index, name='index'),  
]

#"POST /admin/login/?next=/admin/ HTTP/1.1" 302 0