from django.shortcuts import render, redirect
from .form import DataForm 
# Create your views here.
def board(request):
    return render(request, "board_app/board_list.html")

def input_data(request):
    if request.method == "POST":
        sub = request.POST["sub"]
        cont = request.POST["cont"]
        # context = {"sub": sub, "cont": cont}
        print("제목 : ", sub)
        print("내용 : ", cont)
        return redirect('/board')
    return render(request, "board_app/board_input.html")

def input_data2(request):
    # 폼클래스가 탬플릿에 전달될 수 있도록 객체 생성
    form_cls = DataForm
    if request.method == "POST":
        form_cls = DataForm(request.POST)
        if form_cls.is_valid() :
            # sub = request.POST.get("sub", None)
            # cont = request.POST.get("cont", None)
            sub = request.POST["subject"]
            cont = request.POST["content"]
            print("제목 : ", sub)
            print("내용 : ", cont)
            return redirect('/board')
    return render(request, "board_app/board_input2.html", {"form":form_cls})
