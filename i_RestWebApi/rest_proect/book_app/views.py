from django.shortcuts import render
from .forms import BookForm
# Create your views here.
def index(request) :
    return render(request, 'book_app/index.html')

def book_insert(request) :
    #도서정보 입력할 forms를 구성하고 model에 맞는 폼 사용
    form = BookForm()
    return render(request, 'book_app/book_form.html',{'form':form})