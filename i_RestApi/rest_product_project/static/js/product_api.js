$(document).ready(function(){
    $('#list').on('click', function(){ // 도서정보 조회메뉴 a태그에 클릭이벤트 연결
        
        // ajax의 key는 규칙에 의해 정해져 있음음
        $.ajax({
            type:"get", // 전체 도시정보 반환환
            // url:"http://127.0.0.1:8000/rest_prd_app/products/", //요청 apiurl, 함수형 뷰
            url:"http://127.0.0.1:8000/rest_prd_app/cbv/products/", //요청 apiurl, 클래스형 뷰
            datatype:'json', 
            success:function(result){
                //요청 성공 후 실행할 코드
                console.log(result);
                $('#index').empty() // 기존 홈화면 지우기
                $('#resultBox').empty() // 기존 contents 결과 지우기
                // 도서리스트 테이블로 구성, 제목 행 구성
                const str = `
                    <table id="prd_list">  
                        <tr>
                            <th>상품번호</th>
                            <th>상품명</th>
                            <th>가격</th>
                            <th>판매처</th>
                            <th>카테고리</th>
                        </tr>
                ` // 위쪽 태그의 id를 사용하려고 빼준거임
                // 제목행을 content 출력영역에 추가
                $('#resultBox').append(str)

                // 반환 결과가 빈 array[]면
                if(result.length==0){
                    $('#prd_list').append("<tr align='center'><td colspan='7'>상품의 정보가 없습니다.</td></tr></table>")
                }else{
                    for(var i=0; i<result.length; i++){
                        $('#prd_list').append('<tr><td><a class="pk" href="#">' + // tr 시작
                            result[i]["prdno"] + '</td><td>' +
                            result[i]["prdname"] + '</td><td>' +
                            result[i]["prdprice"] + '</td><td>' +
                            result[i]["prdmaker"] + '</td><td>' +
                            result[i]["ctgno"]["ctgname"] + '</td><td>' // tr 종료
                        ) // append 종료
                    } // for문 종료
                } // else 종료
                $('#prd_list').append('</table>'); // 테이블 닫기
            }, // success 
            error:function(){
                //요청 실패 후 실행할 코드
                alert("전송실패:코드확인");
            },
            complete:function(){
                //성공하던 실패하던 종료전에 정리위한 코드
                
            }
    
        });//ajax 끝
    
    });//on 끝

// ================================================================================================================

    // 도서정보 조회 후 도서번호를 클릭하면 1권 도서정보를 api로 받아서 표현
    // 도서번호 동적으로 생성됨, 도서번호에 클릭이벤트 연결 (도서번호는 0~n개 :클래스 선택자를 이용하면 배열로 반환)
    // 위의 방법이 이벤트 연결이 어려워서, 아래의 방법으로로
    $(document).on('click','.pk', function(){ // 도서정보 조회메뉴 a태그(class='pk')에 클릭이벤트 연결
        
        var prdno = $(this).text(); // 현재 클릭한 객체의 내부 text를 추출
        alert(prdno)
        // ajax의 key는 규칙에 의해 정해져 있음음
        $.ajax({
            type:"get", // 전체 도시정보 반환환
            // url:"http://127.0.0.1:8000/rest_prd_app/product/" + prdno + "/", // 함수형 뷰 api url,
            url:"http://127.0.0.1:8000/rest_prd_app/cbv/product/" + prdno + "/", // 클래스형 뷰 api url
            datatype:'json', 
            success:function(result){
                //요청 성공 후 실행할 코드
                console.log(result);
                $('#index').empty() // 기존 홈화면 지우기
                $('#resultBox').empty() // 기존 contents 결과 지우기
                // 도서리스트 테이블로 구성, 제목 행 구성
                const str = `
                    <table id="prd_detail"> <tr><th>상품번호</th><td>`+result["prdno"]+`</td></tr>` +
                                           `<tr><th>상품명</th><td>`+result["prdname"]+`</td></tr>` +
                                           `<tr><th>가격</th><td>`+result["prdprice"]+`</td></tr>` +
                                           `<tr><th>판매처</th><td>`+result["prdmaker"]+`</td></tr>` +
                                           `<tr><th>카테고리</th><td>`+result["ctgno"]["ctgname"]+`</td></tr></table>`
                $('#resultBox').append(str)
            }, // success 
            error:function(){
                //요청 실패 후 실행할 코드
                alert("전송실패:코드확인");
            },
            complete:function(){
                //성공하던 실패하던 종료전에 정리위한 코드
                
            }
    
        });//ajax 끝
    
    });//on 단일 도서 상세 정보 조회 끝
// =======================================================================
// mixin으로 구성한 전체 제품 조회, 신규 생성================================
    $("#prdinsertform").on("submit", function(){
        event.preventDefault();

        var formSerializeArray=$(this).serializeArray();
        console.log(formSerializeArray);

        var object = {};
        
    })

// =======================================================================
// mixin으로 구성한 단일제품 조회, 생성, 수정 삭제========================================
    });//ready 끝