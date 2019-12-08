from django.urls import path

from . import views

app_name = 'smn'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('addNewName/', views.add_new_name, name="addNewName"),
    path('delete/', views.delete_name, name="delete"),    
    path('search/', views.search_name, name="search"),    
]