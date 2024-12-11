from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("product/list/", views.product_list, name="product_list"),
    path("product/detail/<str:prdno>", views.product_detail, name="product_detail"),
# <>을 통해서 파라미터를 전달하게 됨, str로 변수타입을 설정가능 
    path("product/insert/", views.product_insert, name="product_insert"),

]