from rest_framework import serializers
from .models import Book, Publisher

class PublisherSerializer(serializers.ModelSerializer): # model 기반 serializer 생성
    class Meta :
        model = Publisher # model Book 클래스의 fields 중 필요한 fields를 선별
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer): # model 기반 serializer 생성
    # pubno = serializers.ReadOnlyField(source="pubno.pubname") # filed의 요소 재정의, 읽기 전용이라, mixins를 상속받아서 처리하면 아예 속성인식이 안돼서 post는 불가능해짐
    # 필요하다면, fileds 안에 속성을 가공한 새로운 data 추가도 가능, 변경, 수정 모두 가능능
    class Meta :
        model = Book # model Book 클래스의 fields 중 필요한 fields를 선별
        fields = [
            "bookno", 
            "bookname", 
            "bookauthor", 
            "bookprice", 
            "bookdate", 
            "bookstock", 
            "pubno",
        ]
    
    def to_representation(self, instance): # 특정필드에 대한 표현방식만 변경하는 함수, response 시 변경
        response = super().to_representation(instance) # 원래 응답을 받아오는 코드 super() - 부모클래스에서
        # 원 응답 형식 중 pubno 필드의 응답형식만 변경
        # PublisherSerializer 활용해서 pubno 주고 이에 대응되는 pubname데이터 받기
        response["pubno"] = PublisherSerializer(instance.pubno).data
        return response