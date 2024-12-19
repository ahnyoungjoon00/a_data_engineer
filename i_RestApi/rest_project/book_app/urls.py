from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("books/insert/", views.book_insert, name="book_insert")
]
