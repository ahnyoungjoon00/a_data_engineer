from rest_framework import serializers
from .models import Book, Publisher

class PublisherSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Publisher
        fields = "__all__" #model의 모든 필드 포함


class BookSerializer(serializers.ModelSerializer) : # model 기반 serializer 생성
    # pubno = serializers.ReadOnlyField(source="pubno.pubname") # field 재정의(ReadOnlyField) (pubno의 속성을 변경):읽기전용,쓰기에러
    # 위 설정으로는 pubno에 값을 저장할 수 없음(현재 직렬화기를 이용 get, post를 모두 하려면 다른 구현을 해야 함)
    # 1. get/post 각각  serializer 생성
    # 2. pubno의 필드속성을 변경하지 않고 표현형식만 변경: 참조하는 모델의 serializer도 구현해야 함
    class Meta :
        model = Book # model Book 클래스의 fields 중 필요한 fileds만 포함
        fields = [ # 필요하다면 fields의 속성을 수정 사용 가능, 새로운 data도 추가
            "bookno",
            "bookname",
            "bookauthor",
            "bookprice",
            "bookdate",
            "bookstock",
            "pubno", # 외래키
        ]

    #field 상관없이 표현방법만 변경되므로 api통해서 전달되는 data가 변경됨
    def to_representation(self, instance): # 특정필드에 대해 표현방식만 변경하는 함수, response시 변경
        response = super().to_representation(instance) #원래의 응답을 받아오는 코드/super : 부모클래스/ 
        # 원 응답형식 중 pubno 필드의 응답형식만 변경 : PublisherSerializer 활용해서 pubno주고 이 no에 대응되는 데이터 모두 갖고옴
        response["pubno"] = PublisherSerializer(instance.pubno).data #예로 1번 pubno 전달이되면 1번 출판사 레코드가 반환
        return response