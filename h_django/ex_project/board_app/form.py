# django에서 제공하는 forms 패키지의 FORM클래스 상속 받아서 클래스 폼 구현
from django import forms

class DataForm(forms.Form) :

    # form 은 입력데이터 저장,처리 진행, 유동성검증 등 처리함수 등 필요
    # 그렇기 때문에 클래스로 구성해야만 각 과정을 정의해주는게 가능
    # 필요한 입력값 만큼 필드(input 태그) 구성
    subject= forms.CharField(max_length=30, label="제목 ")
    content= forms.CharField(max_length=300, label="내용 ", widget=forms.Textarea)