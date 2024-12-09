from django.shortcuts import render

# Create your views here.
def index(request) : 
    return render(request, "html_app/index.html")

# 각각의 url을 연결해줄 함수
def a(request) :
    return render(request, "html_app/a_hello.html")
def b(request) :
    return render(request, "html_app/b_글자관련태그.html")
def c(request) :
    return render(request, "html_app/c_목록관련태그.html")
def d(request) :
    return render(request, "html_app/d_표관련태그.html")
def e(request) :
    return render(request, "html_app/e_영역관련태그.html")
def f(request) :
    return render(request, "html_app/f_이미지관련태그.html")
def g(request) :
    return render(request, "html_app/g_미디어관련태그.html")
def h(request) :
    return render(request, "html_app/h_하이퍼링크태그.html")
def i(request) :
    return render(request, "html_app/i_form태그.html")
