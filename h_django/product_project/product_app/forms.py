from django import forms
from .models import Product

# class ProductForm(forms.Form) : # 일반 Form 클래스를 상속받아서 
class ProductForm(forms.ModelForm) : # model과 연동되는 form 클래스를 상속해서 사용하겟다.
    class Meta:
        model=Product
        fields=( # Product 모델 필드 중 form에 포함할 필드 나열
            "prdno",
            "prdname",
            "prdprice",
            "prdmaker",
            "prdcolor",
            "ctgno",
        )
        labels = {
            "prdno":"상품번호",
            "prdname":"상품명",
            "prdprice":"상품가격",
            "prdmaker":"제조사",
            "prdcolor":"색상",
            "ctgno":"카테고리",
        }