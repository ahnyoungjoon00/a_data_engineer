from django.shortcuts import render

from rest_framework.response import Response # 응답처리
from rest_framework.views import APIView # 클래스형 view를 API로 구성하는
from rest_framework.decorators import api_view # 함수형 view를 API로 구성하는
from rest_framework import mixins, generics, status
from rest_framework.generics import get_object_or_404

from .models import Book, Publisher
from .serializers import BookSerializer
# Create your views here.

# helloAPI함수는 api로 응답 진행
@api_view(["GET"]) # 이렇게 데코레이터 달아놓으면 api인걸 인식
def helloAPI(request):
    return Response("hello world!") 
# api 전송 데이터는 content-type:application/json 형태로 전송되는거 인지해야함


# 도서 전체 정보 조회 (직렬화 기능을 활용한) : get 방식 요청
# 도서 정보 등록 (직렬화 기능 활용한) : post 방식 요청(data 전송)
# 위의 두가지 기능을 한번에 해주는 함수형 view
@api_view(["GET", "POST"])
def booksAPI(request):
    if request.method=="GET":
        # 도서 전체 정보를 {1}model을 통해서 추출한 후,
        books = Book.objects.all() # 파이썬 장고 모델 객체(레코드 object n개)
        # {2}직렬화 진행, (객체 -> json형식)
        # BookSerializer(books) # 한개 레코드에 대해 직렬화
        
        # 문자열 json파일 상태로
        serializer = BookSerializer(books, many=True) # 다수의 레코드에 대해 직렬화, [{}, {}, ...]형식으로 떨어짐
        # {3}응답 처리
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=="POST":
        # 도서 정보 {1}json형식으로 전달되면, {2}역직렬화 후, {3}serializer를 통해서 {4}model을 거쳐서 db에 저장
        # 클라이언트 -> 서버
        # json문자열 -> 파이썬 객체로 변환(역직렬화)
            # request.POST로 데이터 추출 : 폼데이터 추출, html형식으로 전달된 데이터<QueryDict>
            # request.data로 데이터 추출 : json 형식으로 추출
        
        # 파이썬 drf 객체 상태로
        serializer = BookSerializer(data=request.data) # data = 문자열 값을 인수로 쓰면 역직렬화
        print(request.data) # 저장 위해 전송된 데이터 확인용
        # 모델과 연결된 serializer이기 때문에 유효성 검증 필요(기본키 제약조건, 외래키 제약조건)
        if serializer.is_valid():
            serializer.save()
        # 탬플릿이 없으므로 여기서 redirect를 못함(restAPI쓰는거 자체가 데이터만 건드리는)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # 무조건 response, 내용은 임의설정(status는 포함시키는게 좋음)
            # HTTP_201_CREATED : 자원이(data, img, media든 뭐든) 저장 성공할 시에
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 1권의 도서정보 조회 : bookno 필요(url을 통해 전달)
@api_view(["GET"])        
def bookAPI(request, bno):
    book = get_object_or_404(Book, bookno=bno) # 모델 객체
    seriealizer = BookSerializer(book) # 모델 객체 직렬화 (모델 객체 -> json)
    return Response(seriealizer.data, status=status.HTTP_200_OK)



# 클래스형 뷰=====================================================================================
# 함수형 api view booksAPI와 동일한 처리
class BooksAPI(APIView): # APIview 상속
    # 클래스의 메소드(함수) 
    # get(): 도서 전체정보 
    # post():도서정보 insert 구성
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# 도서 1권 조회만 하는 클래스
class BookAPI(APIView):
    def get(self, request, bno):
        book = get_object_or_404(Book, bookno = bno)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# Minxins class 사용 뷰===========================================================================
# ListModelMixin : 전체 정보 조회와 관련된 클래스
# CreateModelMixin : 정보 생성, 정보 저장과 관련된 클래스
# generics.GenericAPIView : APIview를 상속 받는 것과 비슷한 기능인데 좀더 포괄적이고, db사용이 더 편리한 클래스
class BooksAPIMinxins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView) :
    queryset=Book.objects.all()
    serializer_class=BookSerializer

        # books = Book.objects.all()
        # serializer = BookSerializer(books, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
    # 위에서 만들었던 get코드가 이렇게 간단해진다.
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) # 전체 도서 정보 응답
    
        # serializer = BookSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    # 위에서 만들었던 post코드가 이렇게 간단해진다.
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) # 1개 도서정보 생성(저장)


# 1개 데이터 조회, 수정, 삭제 class 구성 ==========================================================
class BookAPIMinxins(mixins.RetrieveModelMixin, # 조회
                     mixins.UpdateModelMixin, # 수정
                     mixins.DestroyModelMixin, # 삭제
                     generics.GenericAPIView):
    queryset = Book.objects.all() # 모든 object 추출해 놓고 기능에 따라 각 함수에서 사용
    serializer_class = BookSerializer # bookSerializer 모듈 위치를 전달하면 사용은 각 함수에서 필요에 따라 사용
    lookup_field = "bookno" # 기본키 필드 특정해서 조건 매칭시 사용, "where bookno == 1234"

    # 어떤 request method일때, 어떤 클래스가 동작해야하는지에 대한 내용을 함수로 구성
    
    # request.method == get
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) # 1개 조회 기능
    
    # request.method == put
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # request.method == delete
    # delete는 삭제할 도서번호(pk)만 있으면 삭제 가능(레코드의 데이터는 필요 없음) : url을 통해 전달됨
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ===============================================================================================================================
# Generics 패키기 : list(get), create(post), retrieve(get), update(put), destroy(delete) =========================================
# generics.ListAPIView :list_api -> method와 기능을 매칭하는 함수 get(), post(), .. 구성 안해줘도 됨
class BookAPIgenList(generics.ListAPIView, # 조회
                     generics.CreateAPIView, # 생성(저장)
                     ):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

# ===============================================================================================================================
# (retrieve(get), update(put), destroy(delete): 특정 레코드 변수, 도서번호): url에 파라미터 추가되어야함 ============================
class BookAPIgenRetri(generics.RetrieveAPIView,
                      generics.UpdateAPIView,
                      generics.DestroyAPIView,
                      ):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    lookup_field="bookno"

# ===============================================================================================================================
# 검색기능 : filter() 함수를 사용해서 검색을 진행 ==================================================================================
# queryset 속성에서는 사용 불가, 매칭이 안되는 형식이라 ============================================================================
# get_queryset() 상위 클래스에서 상속받아서 오버라이등(부모클래스의 내용을 수정)해서 사용함 ===========================================
# generics.ListAPIView 클래스 : List기능은 가능 / filter() 기능은 포함되어 있지 않음 ===============================================
# filter()를 사용하려면 ListAPIView에 존재하는 get_queryset() 함수를 수정해서 필터기능으로 사용, 검색 진행 ===========================
# 도서명 키워드를 전달 받아서 (url 파라미터로) 해당 도서의 정보를 반환하는 역할을 하는 view 클래스 구성 ================================
# http://127.0.0.1:8000/rest_app/search/장고/
# queryset = model.objexts.filter(검색조건) 형태
class BookSearch(generics.ListAPIView):
    # queryset=Book.objects.filter("검색조건") # 현재 적용이 안되는 상태
    
    serializer_class=BookSerializer

    # 검색어가 1개인 경우 -> url파라미터로 검색어를 전달받아서 -> self 인수에 포함되어져 함수로 전달될 것
    # queryset 대신에 get_queryset()을 오버라이딩해서 검색 진행 후 반환
    # def get_queryset(self):
    #     return super().get_queryset()

    # self(*args, **kwargs:{key:value}) self는 이런식으로 들어옴
    def get_queryset(self):
        return Book.objects.filter(bookname=self.kwargs["keyword"]) # 키워드값과 완전일치하는 레코드를 찾아서 반환
        return Book.objects.filter(bookname__contains=self.kwargs["keyword"]) # 키워드값과 부분일치하는 레코드를 찾아서 반환

    def get(self, request, *args, **kwargs): # get요청을 허용하는 함수
        return self.list(request, *args, **kwargs)