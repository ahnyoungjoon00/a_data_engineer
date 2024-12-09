# 클래스로 우리가 만든 장고 폼을 생성해줘야함
# 장고가 제공하는 패키지 forms를 활용

from django import forms

# class 클래스명(상속받을 패키지 클래스) :
#   클래스내용 

class DataForm(forms.Form): # 기본설정은 Form클래스를 따르겠다. 몇가지 내용을 추가 하는
    # 입력 필드 속성 추가(아래 코드에 의해서 2개의 input태그가 생성됨)
    # input 태그: forms.ChardField(max_length=, label=): 문자, forms.IntegerField(label=) :숫자
    name = forms.CharField(max_length=10, label="이름2")
    age = forms.IntegerField(label="나이2")