from django.shortcuts import render
from rest_framework.decorators import api_view #함수형 view를 api로 만들어 줌
from rest_framework.views import APIView #클래스형 view를 api로 구성
from rest_framework.response import Response #응답처리
from rest_framework import mixins, generics, status
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import get_object_or_404 #특정 조건의 유일한 레코드들 추출



# Create your views here.
# helloAPI 함수는 api로 응답 진행 : @api_view(['요청방식'])
@api_view(['GET']) # get 요청만 처리하도록 api를 구성
def helloAPI(request) :
    return Response("hello world! 안녕") # api 전송 data는 content-type : application/json

# 도서 전체 정보 조회 (직렬화 기능 활용) : get 요청
# 도서 정보 등록(직렬화 기능 활용) : post 요청(data 전송)
# 함수형 view
@api_view(['GET','POST'])
def booksAPI(request) :
    if request.method == "GET" : # 객체 list
        # 도서전체정보를 1.model 통해서 추출한 후에 2.직렬화 진행 3응답처리
        books = Book.objects.all() #파이썬 장고 모델 객체 (레코드 object : 0~n개)

        # 객체 -> JSON : 직렬화
        #BookSerializer(books)  # 한개 레코드에 대해 직렬화
        serializer = BookSerializer(books,many=True) #many=True : 다수의 데이터를 한번에 serializer [{},{}] 반환
        #serializer 문자열 JSON을 담고 있는 객체
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST": # 객체 create
        # 도서정보 1. request data가 json 형식으로 전달되면 2. 역직렬화후 3. serializer(모델) 통해서 db에 저장
        # 클라이언트 -> 서버
        # JSON 문자열 -> 파이썬 객체로 변환(역직렬화)
        # request.POST : 폼데이터 추출, html 형식으로 전달된 데이터<QueryDict>
        # request.data : json 형식으로 추출
        serializer = BookSerializer(data=request.data) # data=문자열값 를 인수로  쓰면 역직렬화
        print(request.data) #저장위해 전송된 데이터 확인용
        # serializer변수 형식 : 파이썬 drf 객체(JSON 없음)
        # 모델과 연결된 serializer기 때문에 유효성 검증을 진행해야 함(기본키 제약조건, 외래키 제약조건
        print(request.data)
        if serializer.is_valid() :
            # 검증완료 후 
            serializer.save() # 모델 통해서 db에 저장(Bookserializer가 생성시 Model을 기반으로 생성)
            # 템플릿 없으므로 리디렉트 불가능 : Response 해야함
            # 201_CREATED : 자원 저장 성공
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 응답은 반드시 처리, 내용은 임의설정(status는 포함시키는것이 좋음)
        else : # 검증 실패
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # data 전송 오류 : 잘못된 형식의 data거나 유효성 위배되는 data

# 1권 도서정보 조회 : bookno 필요(url 통해서 전달)
@api_view(['GET'])        
def bookAPI(request, bno) :
    book = get_object_or_404(Book, bookno=bno) #book: 모델 객체 bookno:model 필드명 bno:url에 의해 전달될 파라미터
    serializer = BookSerializer(book) #모델객체 book 직렬화 : serializer json 담고 있는 객체
    return Response(serializer.data, status=status.HTTP_200_OK)

#함수형 뷰 종료###################################

#클래스형 뷰 시작 ################################
#함수형 api view bookdsAPI와 동일 처리
#전체 도서 정보 조회 및 create
class BooksAPI(APIView) : #APIView 상속
    # 클래스 메소드(함수) get():도서 전체정보 post():도서 정보 insert 구성
    def get(self,request) :
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True) # books 객체의 모든 레코드 object json 변환
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request) :
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid() : 
            serializer.save() #serializer -> model -> db 까지 전달
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# 도서 1권 조회만 하는 클래스
class BookAPI(APIView) : 
    def get(self,request,bno) : #get 요청으로 1권 도서 조회(도서번호 필요)
        book = get_object_or_404(Book, bookno=bno)
        serializer = BookSerializer(book) #클래스 생성자함수를 이용해서 객체
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#############  Mixins class 사용 뷰 #################################
# ListModelMixin : 전체정보조회
# CreateModelMixin : 정보생성 또는 저장
# GenericAPIView : 클래스를 api view로 구성, DB 사용 편리하게
class BooksAPIMixins(mixins.ListModelMixin, 
                     mixins.CreateModelMixin,
                     generics.GenericAPIView) : 
    queryset = Book.objects.all() #일반 APIView는 queryset 속성이 없음,GenericAPIView
    serializer_class = BookSerializer # 클래스레벨 속성에 serializer 등록해놓고 각 메소드에서는 serializer_classc 참조해서 구현 
    # 현재 api뷰에서 사용할 serializer 설정
    
        # books = Book.objects.all()
        # serializer = BookSerializer(books,many=True) # books 객체의 모든 레코드 object json 변환
        # return Response(serializer.data, status=status.HTTP_200_OK)
    def get(self, request, *args, **kwargs) : 
        return self.list(request, *args, **kwargs) # 전체 도서정보 응답
    
        # serializer = BookSerializer(data=request.data)
        # if serializer.is_valid() : 
        #     serializer.save() #serializer -> model -> db 까지 전달
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    def post(self, request, *args, **kwargs) :
        return self.create(request, *args, **kwargs) # 1개 도서정보 생성(저장)

#########################################################################
# 1개 데이터 조회, 수정, 삭제 class BookAPIMixins : MixIns 사용

class BookAPIMixins(mixins.RetrieveModelMixin, #1개데이터 조회기능 클래스
                    mixins.UpdateModelMixin, # 수정
                    mixins.DestroyModelMixin, # 삭제
                    generics.GenericAPIView) : # ApiView : generic은 mixin이나 db관련한 더 많은 기능 제공
    
    queryset = Book.objects.all() # 모든 object 추출해 놓고 기능에 따라 각 함수에서 사용
    serializer_class = BookSerializer #BookSerializer 모듈 위치를 전달하면 사용은 각 함수에서 필요에 따라 사용
    lookup_field = 'bookno' #기본키필드 특정해서 조건 매칭시 사용 where bookno = 1234

    # 어떤 request method일때 어떤 클래스가 동작해야 하는지에 대한 내용을 함수로 구성하게 됨
    # 함수명이 method명 이어야 함
    # request.method == get
    def get(self,request, *args, **kwargs) :
        return self.retrieve(request,*args, **kwargs) #1개 데이터 조회기능 완성
    
    # request.method == put (수정할 data가 전달됨 : 헤더를 통해 전달됨(request.data))
    # *args, **kwargs 함수 인수는 url 파라미터를 받는데 사용
    def put(self, request, *args, **kwargs) : 
        return self.update(request, *args, **kwargs)#1개 데이터 수정기능 완성
    
    # request.method == delete
    # delete는 삭제할 도서번호(pk)만 있으면 삭제가 가능(레코드의 데이터는 필요없음) : url을 통해 전달됨
    def delete(self, request, *args, **kwargs) :
        
        return self.destroy(request, *args, **kwargs)#1개 데이터 삭제기능 완성

#################################################################################
## Generics 패키지 : list(get),create(post),(retrieve(get),update(put),destory(delete):특정 레코드 변수,도서번호)
## generics.ListAPIView : list+api -> method와 기능을 매칭시키는 함수 get() 구성하지 않아도 됨
## generics.CreateAPIView : create+api -> method와 기능을 매칭시키는 함수 post() 구성하지 않아도 됨
class BookAPIgenList(generics.ListAPIView, #xxxapiview 클래스 추가 만으로 기능이 구현이 됨
                     generics.CreateAPIView): 
    queryset=Book.objects.all()
    serializer_class=BookSerializer    

###################################################################################
## (retrieve(get),update(put),destory(delete):특정 레코드 변수,도서번호) : url에 파라미터 추가되어야 함
class BookAPIgenRetri(generics.RetrieveAPIView,
                      generics.UpdateAPIView,
                      generics.DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer        
    lookup_field='bookno' #lookup 필드와 이름이 같은 파라미터변수가 url에 포함되어있어야 함

