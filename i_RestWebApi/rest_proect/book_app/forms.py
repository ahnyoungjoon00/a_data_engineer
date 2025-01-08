from django import forms
from rest_app.models import Book # 다른 앱의 모듈 참조방법 앱이름.모듈

# ModelForm 클래스 상속 받음
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'bookno',
            'bookname',
            'bookauthor',
            'bookprice',
            'bookdate',
            'bookstock',
            'pubno'
        )
        
        labels = {
            'bookno':'도서번호',
            'bookname':'도서명',
            'bookauthor':'저자',            
            'bookprice':'도서가격',
            'bookdate':'출판일',
            'bookstock':'재고',
            'pubno':'출판사'
        }
