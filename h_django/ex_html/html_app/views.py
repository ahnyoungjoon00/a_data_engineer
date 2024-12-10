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

def j(request) :
    if request.method == "POST" :
        print(request.POST)
        date = request.POST["date"]
        habbit = request.POST["habbit"]
        activity = request.POST["activity"] # 체크 박스에서 이렇게 데이터를 받으면 여러개 데이터 중에 마지막 입력값만 받아짐
        exercise = request.POST.getlist("exercise") # 다중데이터인 경우 POST.getlist()함수를 이용
        print(date, habbit, exercise, activity)
        context = {"date": date, "habbit": habbit, "exercise":exercise}
        # form 태그 안의 name속성이 없다면 데이터가 전송되지 않는다.
    return render(request, "html_app/j_formres.html", {"ctx":context})
