from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("add_stoke/",views.add_stock, name="add_stoke"),
]