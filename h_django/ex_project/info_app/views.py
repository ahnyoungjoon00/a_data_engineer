from django.shortcuts import render

# Create your views here.
def index(request) : 
    return render(request, "info_app/index.html")
def show_info(request) : # html 내에 js를 포함시켜 놓으면, 장고탬플릿도 해석이 가능해서 처리 가능해짐
    return render(request, "info_app/info.html")
def show_info2(request) : # 이렇게 외부 js로 해놓으면 js는 장고탬플릿을 몰라서 입력값 그대로를 전송해버림
    return render(request, "info_app/info2.html")