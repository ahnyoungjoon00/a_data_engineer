from django import forms
from rest_product_app.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=(
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
            "prdmaker":"생산처",
            "prdcolor":"색상",
            "ctgno":"카테고리번호",
            }
        