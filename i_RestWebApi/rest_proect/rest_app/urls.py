from django.urls import path
from . import views

urlpatterns = [
    path("hello/",views.helloAPI), #test api url
    path("books/",views.booksAPI), # http://127.0.0.1:8000/rest_app/books/ : 브라우저 주소줄 통해 get 방식 요청진행
    path("book/<int:bno>/",views.bookAPI), # http://127.0.0.1:8000/rest_app/book/1003/ ->도서번호 get방식 요청
    path("cbv/books/",views.BooksAPI.as_view()), #class를 view로 변환 : as_view()
    path("cbv/book/<int:bno>/", views.BookAPI.as_view()),
    path("mixin/books/",views.BooksAPIMixins.as_view()),
    path("mixin/book/<int:bookno>/", views.BookAPIMixins.as_view()), # url변수명은 model의 기본키필드명과 동일하게 구성
    path("generic/books/", views.BookAPIgenList.as_view()),
    path("generic/book/<int:bookno>/",views.BookAPIgenRetri.as_view()),
]