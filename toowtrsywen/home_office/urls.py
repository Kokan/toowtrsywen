from django.urls import path
from django.urls import include, path
from . import views

app_name = "home_office"

urlpatterns = [
    path('home_office/', views.homeoffice_view, name="homeoffice_view")
]