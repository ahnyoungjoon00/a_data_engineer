from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.prdsAPI),
    path("product/<int:prd_no>/",views.prdAPI),
    path("cbv/products/", views.ProductsAPI.as_view()), # as_view() :클래스 내부에 있는 함수들을 실행할수 있게 api뷰 컨트롤러로 구성함
    path("cbv/product/<int:prd_no>/", views.ProductAPI.as_view()),
]