from django.shortcuts import render
from rest_framework.decorators import api_view # 함수형 컨트롤러(view)를 @(데코레이터)를 이용해서 api 컨트롤러로 변한
from rest_framework.views import APIView # 클래스형컨트롤러에 api 기능을 부여하는 클래스(상속받아서 사용)
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import get_object_or_404

# Create your views here.
# 보통 api 컨트롤러(view)구현할 때 암묵적으로 get요청에 대해서는 조회를 위한 데이터를 전송
# post 요청에 대해서는 넘겨받은 자원을 서버에 생성:create(db에 insert)으로 약속되어 있음
# 단, update, delete에 대해서는 요청 method를 따로 구성해 놓음
# update:PUT, delete : DELETE

######### 함수형 뷰 ################################
@api_view(['GET','POST'])
def prdsAPI(request) :
    if request.method == "GET" : #전체 상품정보 조회 후 직렬화 후 데이터 전송
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True) #직렬화 다수의 오브젝트 직렬화 후 list에 저장해서 반환
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST" : #1개 상품데이터전송받아 역직렬화 후 db에 insert(create)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save() # 모델통해 db 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def prdAPI(request, prd_no) : #한개의 상품정보만 조회하는 기능
    product = get_object_or_404(Product, prdno=prd_no)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

########## 클래스형 뷰 ####################################
class ProductsAPI(APIView) : #prdsAPI와 동일기능하는 클래스형 API 뷰
    def get(self,request) : # 전체상품정보조회
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True) #직렬화 다수의 오브젝트 직렬화 후 list에 저장해서 반환
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request) : #한개상품 정보 insert(creat)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save() # 모델통해 db 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 한개의 상품정보 조회        
class ProductAPI(APIView) :
    def get(self,request,prd_no) :
        product = get_object_or_404(Product, prdno=prd_no) # 특정상품 db에서 추출
        serializer = ProductSerializer(product) #직렬화 -> json
        return Response(serializer.data, status=status.HTTP_200_OK) #요청객체에전송
        


