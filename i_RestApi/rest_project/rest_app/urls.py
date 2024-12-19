
from django.urls import path
from . import views
urlpatterns = [
    path("hello/", views.helloAPI),
    path("books/", views.booksAPI),
    path("book/<int:bno>/", views.bookAPI),

    path("cbv/books/", views.BooksAPI.as_view()), # 클래스를 뷰로 변환하는 함수 as_view()
    path("cbv/book/<int:bno>/", views.BookAPI.as_view()),

    path("mixin/books/", views.BooksAPIMinxins.as_view()),
    path("mixin/book/<int:bookno>/", views.BookAPIMinxins.as_view()), # url변수명은 model의 기본키필드명과 동일하게 구성
    
    path("generic/books/", views.BookAPIgenList.as_view()), # url변수명은 model의 기본키필드명과 동일하게 구성
    path("generic/book/<int:bookno>/", views.BookAPIgenRetri.as_view()),

    path("book/search/<str:keyword>/", views.BookSearch.as_view()), 
    # http:127.0.0.1:8000/rest_app/book/search/장고/ 형태로 요청
    # {"keyword":"장고"}형식으로 전달받게 됨

]
