from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer): # model 기반 serializer 생성
    # ctgno = serializers.ReadOnlyField(source="ctgno.ctgname") # filed의 요소 재정의
    # 필요하다면, fileds 안에 속성을 가공한 새로운 data 추가도 가능, 변경, 수정 모두 가능능
    class Meta :
        model = Product # model Book 클래스의 fields 중 필요한 fields를 선별
        fields = [
            "prdno", 
            "prdname", 
            "prdprice", 
            "prdmaker", 
            "ctgno", 
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"