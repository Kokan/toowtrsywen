from django.urls import path
from django.urls import include, path
from . import views

app_name = "check_in_out"

urlpatterns = [
    path('check_in_out/', views.main_text, name="main_text"),

]