from django.urls import path
from django.urls import include, path
from . import views
from rest_framework import routers

app_name = "check_in_out"
router = routers.DefaultRouter()
router.register('check_in_out',views.CheckTimeView)

urlpatterns = [
    # path('check_in_out/', views.main_text, include(router.urls),name="main_text"),
    path('check_in_out/', include(router.urls)),

]