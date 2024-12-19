from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("products/insert", views.prd_insert, name='prd_insert'),
]
