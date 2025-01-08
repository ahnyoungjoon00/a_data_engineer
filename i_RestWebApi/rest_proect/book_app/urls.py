from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("book/insert/", views.book_insert, name="insert"),
]