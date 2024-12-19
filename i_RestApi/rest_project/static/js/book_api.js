$(document).ready(function(){
    $('#list').on('click', function(){ // 도서정보 조회메뉴 a태그에 클릭이벤트 연결
        
        // ajax의 key는 규칙에 의해 정해져 있음음
        $.ajax({
            type:"get", // 전체 도시정보 반환환
            // url:"http://127.0.0.1:8000/rest_app/books/", //요청 apiurl, 함수형 뷰
            url:"http://127.0.0.1:8000/rest_app/cbv/books/", //요청 apiurl, 클래스형 뷰
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
                            <th>도서번호</th>
                            <th>도서명</th>
                            <th>저자</th>
                            <th>도서가격</th>
                            <th>출판일</th>
                            <th>재고</th>
                            <th>출판사</th>
                            <th>수정</th>
                            <th>삭제</th>
                        </tr>
                ` // 위쪽 태그의 id를 사용하려고 빼준거임
                // 제목행을 content 출력영역에 추가
                $('#resultBox').append(str)

                // 반환 결과가 빈 array[]면
                if(result.length==0){
                    $('#prd_list').append("<tr align='center'><td colspan='7'>도서의 정보가 없습니다.</td></tr></table>")
                }else{
                    for(var i=0; i<result.length; i++){
                        $('#prd_list').append('<tr><td><a class="pk" href="#">' + // tr 시작
                            result[i]["bookno"] + '</td><td>' +
                            result[i]["bookname"] + '</td><td>' +
                            result[i]["bookauthor"] + '</td><td>' +
                            result[i]["bookprice"] + '</td><td>' +
                            result[i]["bookdate"] + '</td><td>' +
                            result[i]["bookstock"] + '</td><td>' +
                            result[i]["pubno"]["pubname"] + '</td>' +
                            '<td><button class="btn" opt="'+result[i]['bookno']+'">수정</button></td>' +
                            '<td><button class="btn2" opt="'+result[i]['bookno']+'">삭제</button></td>' +
                            '</tr>' // tr 종료
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
        
        var bno = $(this).text(); // 현재 클릭한 객체의 내부 text를 추출
        alert(bno)
        // ajax의 key는 규칙에 의해 정해져 있음음
        $.ajax({
            type:"get", // 전체 도시정보 반환환
            // url:"http://127.0.0.1:8000/rest_app/book/" + bno + "/", // 함수형 뷰 api url,
            url:"http://127.0.0.1:8000/rest_app/cbv/book/" + bno + "/", // 클래스형 뷰 api url

            datatype:'json', 
            success:function(result){
                //요청 성공 후 실행할 코드
                console.log(result);
                $('#index').empty() // 기존 홈화면 지우기
                $('#resultBox').empty() // 기존 contents 결과 지우기
                // 도서리스트 테이블로 구성, 제목 행 구성
                const str = `<table id="prd_detail"> <tr><th>도서번호</th><td>`+result["bookno"]+`</td></tr>` +
                                                    `<tr><th>도서명</th><td>`+result["bookname"]+`</td></tr>` +
                                                    `<tr><th>저자</th><td>`+result["bookauthor"]+`</td></tr>` +
                                                    `<tr><th>도서가격</th><td>`+result["bookprice"]+`</td></tr>` +
                                                    `<tr><th>출판일</th><td>`+result["bookdate"]+`</td></tr>` +
                                                    `<tr><th>재고</th><td>`+result["bookstock"]+`</td></tr>` +
                                                    `<tr><th>출판사</th><td>`+result["pubno"]+`</td></tr></table>`
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
    
    });//on 도서 상세보기 끝
// ================================================================================================================
    // 도서정보 등록 완료와 관련된 js ajax이용 post 통신, form data를 json으로 변경
    // 도서정보 등록 완료 후 도서정보 조회 메뉴로 강제 전환
    // 도서정보 입력 후 등록버튼 클릭하면 아래 함수 진행
    $('#bkinsertform').on('submit', function(){
        event.preventDefault();

        // #bkinsertform 안의 data를 추출해서 json형식으로 변경
        var formSerializeArray = $(this).serializeArray();
        console.log(formSerializeArray);

        var object = {};
        for(var i=0; i<formSerializeArray.length; i++){
            object[formSerializeArray[i]["name"]] = formSerializeArray[i]["value"];
        }
        console.log(object);
        var json = JSON.stringify(object);
        console.log(object);

        $.ajax({
            type:"post", // api의 create(insert)기능을 사용
            url:"http://127.0.0.1:8000/rest_app/mixin/books/",
            data:json,
            datatype:"json",
            contentType:"application/json; charset-utf-8",
            success:function(result){
                console.log(result);
                $("#index").empty();
                $("#resultBox").empty();
                $("#list").trigger("click");
            },
            error:function(){
                alert("전송실패 또는 데이터입력 실패")
            }
        }) // ajax 끝
    }); // submit on 끝

// ===============================================================================================================================
// 도서 정보 수정버튼 클릭 시, 생성되는 수정 from ===================================================================================
// 수정버튼 동적으로 생성 : 버튼에 직접 click 이벤트 연결 불가능 -> document를 통해서 간접적 이벤트 연결
// {1} 특정도서 도서번호 추출
// {2} 도서번호가 포함된 api ajax 요청
// [3] 서버로부터 전송된 도서번호의 data를 화면에 출력(태그포함)
    $(document).on("click", '.btn', function(){
        event.preventDefault();
        bookno = $(this).attr("opt"); // attr(속성명) :속성의 값을 반환
        alert(bookno);
        // api 데이터 요청 : mixin 기능으로 생성된 뷰애게 요청(1개 도서에 대한 데이터 요청)
        $.ajax({
            type:"get",
            url:"http://127.0.0.1:8000/rest_app/mixin/book/" + bookno + "/",
            datatype:"json", // 서버 -> 클라이언트로 가는 data의 타입
            contentType:"application/json; charset=utf-8", // 아마 넘어가는 컨텐츠는 없을건데 그냥 써놓는다.
            success:function(result){
                console.log(result);
                // 성공했을때 전달되는 도서 1권의 정보를 수정 가능하게 태그를 이용해서 표현, 완료버튼 추가
                // 전송할 data를 쉽게 추출하도록 form태그 안에 표현
                $("#index").empty();
                $("#resultBox").empty();
                $("#index").append("<h2>도서정보수정</h2>")
            
                const str = '<form id="updateFrm"><table id="prd_detail">' +
                '<tr><th>도서번호</th><td><input type="text" name="bookno" value="'+result["bookno"]+'"></td></tr>' +
                '<tr><th>도서명</th><td><input type="text" name="bookname" value="'+result["bookname"]+'"></td></tr>' +
                '<tr><th>저자</th><td><input type="text" name="bookauthor" value="'+result["bookauthor"]+'"></td></tr>' +
                '<tr><th>도서가격</th><td><input type="text" name="bookprice" value="'+result["bookprice"]+'"></td></tr>' +
                '<tr><th>출판일</th><td><input type="text" name="bookdate" value="'+result["bookdate"]+'"></td></tr>' +
                '<tr><th>재고</th><td><input type="text" name="bookstock" value="'+result["bookstock"]+'"></td></tr>' +
                '<tr><th>출판사</th><td><input type="text" name="pubno" value="'+result["pubno"].pubname+'"></td></tr>' +
                '</table>'+
                '<button id="update" class="btn" opt="'+ result["bookno"] +'">완료</button>' +
                '</form>'
                $('#resultBox').append(str)
                // 데이터 표현 태그
            },
            error:function(){
                alert("전송실패 또는 data 반환 실패")
            }
        })

    }); // 도서정보수정버튼 클릭 끝
// ===============================================================================================================================
// 도서 정보 수정 완료 기능, 완료버튼 클릭시 실행되는 함수============================================================================
    $(document).on("click", "#update", function(){
        event.preventDefault();
        
        // {1} 완료버튼에 추가된 도서번호 추출
        var bookno=$(this).attr("opt");
        
        // {2} 수정정보 폼에서 추출 후, json으로 변경
        var formSerializeArray=$("#updateFrm").serializeArray(); // key:value 타입의 array[{name:"bookno", value:"1001"}, {name:bookname, value:"SQLD학개론"}, ...] 구성
        var object={};
        for (var i=0; i<formSerializeArray.length; i++){
            object[formSerializeArray[i]["name"]] = formSerializeArray[i]["value"]; // [{"bookno":"1001"}, ...]
        }
        var json=JSON.stringify(object);
        console.log(json);
        // {3} api 요청해서 도서 수정 ajax 구성
        $.ajax({
            type:"PUT",
            url:"http://127.0.0.1:8000/rest_app/mixin/book/" + bookno + "/",
            data:json,
            contentType:"application/json; charset=utf-8",
            success:function(result){
                console.log(result);
                $("#index").empty();
                $("#resultBox").empty();
                $("#list").trigger("click") //도서 정보 조회 메뉴 강제 실행
            },
            error:function(){
                alert("전송실패 또는 data 오류")
            }
        }) // ajax 끝
    }) // 도서정보수정완료 끝

// ===============================================================================================================================
// 도서 정보 삭제 기능=============================================================================================================
    // {1} 도서번호 추출
    $(document).on("click", ".btn2", function(){
        event.preventDefault();
        bookno = $(this).attr("opt");

        if(confirm(bookno + "의 정보를 삭제하시겠습니까?")){
        // 메시지에서 예(true) 선택 시, 삭제 진행
            $.ajax({
                type:"DELETE",
                url:"http://127.0.0.1:8000/rest_app/mixin/book/"+bookno+"/",
                datatype:"json",
                contentType:"application/json; charset=utf-8",
                success:function(result){
                    $("#list").trigger("click"); // 강제로 클릭 이벤트 발생(도서정보조회 새로 요청)
                },
                error:function(){
                    alert("전송 실패 또는 삭제 실패")
                }
            }); // ajax 끝
        }

    // {2} 삭제할건지 확인 메시지 창
    // {3} ajax 사용 삭제 api 호출 후, 도서정보조회로 이동

    })

});//ready 끝