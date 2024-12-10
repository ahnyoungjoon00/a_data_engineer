from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("info/", views.show_info, name="show_info"),
    path("info2/", views.show_info2, name="show_info2"),
]