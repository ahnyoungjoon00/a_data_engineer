from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.board, name="board"),
    path("input/", views.input_data, name="input"),
    path("input2/", views.input_data2, name="input2"),

]