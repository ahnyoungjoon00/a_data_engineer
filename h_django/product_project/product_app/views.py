from django.shortcuts import render,get_object_or_404, redirect
from .models import Product # product 테이블의 구성은 model의 product 클래스에서 해놓음
from .forms import ProductForm
import pandas as pd
# Create your views here.
def index(request) :
    return render(request, "product_app/index.html")

# def product_list(request):
#     # django_db의 product 테이블에서 모든 레코드 추출 후 탬플릿에 전달
#     # django ORM 사용 : model 사용
#     # class.objects.all() == select * from product테이블
#     products = Product.objects.all()
#     # queryset dic 형식으로 받아옴 -> 장고는 이를 인식해서 탬플릿(형식) 그대로 사용 가능
#     print(products) # 이러면 object 형태로 출력되어 내용이 표출 안됨
#     print(Product.objects.values()) # db레코드는 딕셔너리로 구성되고 전체 레코드가 리스트에 담겨있음
#     return render(request, "product_app/product_list.html", {"products": products})

# 문자열 컬럼인 prdno를 수치형으로 변경하여 정렬하기 위해
def product_list(request):
    products = Product.objects.all()
    # print(Product.objects.values())
    
    # 리스트 변수로 담기위해
    prd_list = []
    for prd in products.values() :
        prd_list.append(prd) # dict 형태의 데이터 한줄씩 리스트에 담음
    # print(prd_list)
    df = pd.DataFrame.from_dict(prd_list)
    df["prdno"] = df["prdno"].astype(int)
    df = df.sort_values("prdno", ascending=True)
    # print(df)
    products_dict = df.to_dict("records")
    print(products_dict)
    return render(request, "product_app/product_list.html", {"products": products_dict})

def product_detail(request, prdno):
    product = get_object_or_404(Product, pk=prdno)
    return render(request, "product_app/product_detail.html", {"product":product})


# 상품 등록 처리
# 요청이 get방식이면 -> 입력 폼을 전달(탬플릿 랜더링)
# 요청이 post방식이면 -> form에서 전송된 데이터 유효성 검증 후, 유효하면 db에 insert후, 상품 정보 조회 컨텐츠로 전환
#                       데이터 입력 후, 완료버튼을 클릭하면
def product_insert(request) :
    form=ProductForm()
    # {1} 요청이 post인지 확인하고
    if request.method == "POST" :
        # {2} 폼데이터의 내용을 변수에 저장(폼클래스 형식으로 저장)
        form = ProductForm(request.POST)
        # {3} Django form의 기본 기능은 is_valid()를 사용해서 데이터 유효성 확인
        if form.is_valid() :
            # 유효성의 위배사항이 없으면 form을 통해 저장(save) : commit되지 않은 상태
            # {4} form.save()를 통해 commit되지 않은 insert를 진행 -> 결과변수에 저장
            product = form.save(commit=False)
            # {5} db에 반영
            product.save()
            # {6} 저장확인을 위해서 상품조회 화면으로 이동
            return redirect("product_list")
    return render(request, "product_app/product_form.html", {"form":form})