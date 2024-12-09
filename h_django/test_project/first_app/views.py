from django.shortcuts import render, redirect
from .forms import DataForm

# Create your views here.
def index(request) : 
    # url 처리 함수는 반드리 request 객체를 인수로 받아야 함
    # Django로부터 url을 통해서 first_app에 요청을 하고
    # first_app의 urls.py에서는 받은 요청 처리를
    # "view.index" => view.py의 index 함수로 전달해서
    # 처리하겠다고 정의했기때문에 뭘하라는지 꼭 받아야함

    # 현재 요청에 대한 처리는 index.html파일을 찾아서 응답을 진행
    # 장고 응답 프로세스인 rendering을 거쳐서 응답을 진행
    return render(request, "first_app/index.html")
           # 응답 대상은 request 객체 변수 안에 저장되어 있기때문에
           # request를 되돌리면 Django가 정보는 알아서 읽어서 응답 대상에게 전달함
           
def show_img(request) :
    # 임의의 데이터 (이름과 나이 데이터) : 예제는 {key:value}형태로, 다른 형식도 가능하다.
    member = {}
    member["name"] = "aaa"
    member["age"] = 10
    members = [
        {"name":"bbb", "age":22}, 
        {"name":"ccc", "age":33},
        {"name":"ddd", "age":44},
        ]
    # member 데이터를 render 함수의 세번째 인수로 전송, {"전송데이터명":전송데이터값(변수 사용)}
    return render(request, "first_app/img.html", {'context':members}) # template 디렉터리는 구성상 기본이라 써줄 필요가 없다.

# def show_img(request) :
#     return render(request, "first_app/img.html") # template 디렉터리는 구성상 기본이라 써줄 필요가 없다.

# 사용자 정의 폼에서 전송된 데이터 처리 함수
# 전송된 데이터 request 파라미터로 전달됨
def data_form(request):
    # get 방식 요청에 대해서는 html페이지를 랜더링
    # return render(request, "first_app/data_form.html")
    # post 방식 요청에 대해서는 전송된 데이터를 출력하고 html페이지 랜더링
    if request.method == "POST":
        print(request.POST) # request객채는 method가 post 방식이면 POST속성이 저장되어 있음
        name = request.POST["name"] # request에 클라이언트가 저장한 name속성 값
        age = request.POST["age"]
        print("이름: ", name)
        print("나이: ", age)
    return render(request, "first_app/data_form.html")

# 폼클래스로 생성된 폼데이터 전송 처리 함수
def data_form2(request):
    # 장고 클래스 form 객체 생성, 클래스가 있는 파일을 import 해줘야함
    # DataForm 클래스를 html파일로 전달해 렌더링
    form = DataForm()
    # method가 post면 전송된 데이터를 터미널에 출력 후, index페이지로 강제 전환 -> redirect()
    if request.method == "POST" :
        print(request.POST) # dict형태로 전송됨
        form_res = DataForm(request.POST) # 서버로 전송된 데이터를 폼클래스 데이터로 변환(Form의 유효성 검증 기능을 사용하기 위해)
        # 전송된 form 데이터 유효성 검증
        if form_res.is_valid() : # 유효성과 관련된 에러가 없으면
            name = request.POST.get("name", None) # request에 클라이언트가 저장한 속성 값을 받는 다른 방식
            age = request.POST.get("age", None)   # .get(key, key값이 없을때 반환할 값)
            print("이름: ", name)
            print("나이: ", age)
            return redirect('/') # index 페S이지로 넘어가게 강제 전환
    return render(request, "first_app/data_form_class.html", {"form": form})
