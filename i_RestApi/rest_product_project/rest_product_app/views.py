from django.shortcuts import render

from rest_framework.response import Response # 응답처리
from rest_framework.views import APIView # 클래스형 view를 API로 구성하는
from rest_framework.decorators import api_view # 함수형 view를 API로 구성하는
from rest_framework import mixins, generics, status
from rest_framework.generics import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
# Create your views here.
# def index(request):
#     return render(request, "rest_product_app/index.html", name="index")

# 함수형 뷰 ###################################################################################################

@api_view(["GET", "POST"])
def prdsAPI(request):
    if request.method=="GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=="POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET"])
def prdAPI(request, prd_no):
    product = get_object_or_404(Product,prdno=prd_no)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 클래스형 뷰 ###################################################################################################

class ProductsAPI(APIView): # prdsAPI와 동일기능 구현
    def get(self, request): # 전체 상품 정보 조회 (select)
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request): # 단일 상품 정보 등록 (insert)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductAPI(APIView) :
    def get(self, request, prd_no):
        product = get_object_or_404(Product, prdno=prd_no)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Mixins활용한 클래스 뷰 ###################################################################################################


class ProductsAPIMinxins(mixins.ListModelMixin, # 전체 조회
                         mixins.CreateModelMixin, # 신규 생성(저장)
                         generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ProductAPIMinxins(mixins.RetrieveModelMixin, # 단일 조회
                        mixins.UpdateModelMixin, # 단일 수정
                        mixins.DestroyModelMixin, # 단일 삭제
                        generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="prdno"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# generic 활용한 클래스 뷰 ###################################################################################################


class ProductAPIgenList(generics.ListAPIView, # 전체 조회
                        generics.CreateAPIView): # 신규 생성(저장)
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
class ProductAPIgenRetri(generics.RetrieveAPIView, #1개 조회
                         generics.UpdateAPIView, # 단일 수정
                         generics.DestroyAPIView # 단일 삭제
                         ): 
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="prdno"
