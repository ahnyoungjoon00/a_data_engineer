from django.contrib import admin
from django.urls import path, include
from . import views # 현재 디렉터리 내의 views.py을 import

urlpatterns = [
    # https://127.0.0.1:8000 요청이 들어오면 first_app의 urls.py 파일을 참조하라
    path("", views.index, name="index"), 
    
    # https://127.0.0.1:8000의 기본 url에 내가 지정한 img/를 합해서
    # https://127.0.0.1:8000/img/ 의 형태로 만들어줌, 앞에 "/"는 작성 ㄴㄴ
    path("img/", views.show_img, name="show_img"), 

    # 사용자 정의 폼, 데이터 처리 url 등록
    path("data/form/", views.data_form, name="data_form"), # https://127.0.0.1:8000/data/form

    # form class 사용, 데이터 처리 url
    path("data/form2/", views.data_form2, name="data_form2"), # https://127.0.0.1:8000/data/form2

]