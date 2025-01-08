$(document).ready(function(){
    $('#list').on('click', function(){ //도서정보조회메뉴 a태그(id=list)에 클릭이벤트 연결

        //ajax의 key는 규칙에 의해 정해져 있음
        $.ajax({
            type:"get", //전체 도서정보 반환
            //url:"http://127.0.0.1:8000/rest_app/books/", //요청 url(api url), 함수형 뷰 api
            url:"http://127.0.0.1:8000/rest_app/cbv/books/", //class형 뷰 api
            datatype:'json', 
            success:function(result){
                //요청 성공 후 실행할 코드
                console.log(result); //데이터 전송되었는지 확인
                $('#index').empty(); //기존 홈 화면 지우기                
                $('#resultBox').empty(); //contents 출력 영역 기존 데이터 지움
                $('#index').append("<h2>도서 정보 조회</h2><br>")
                //도서 리스트 테이블로 구성, 제목 행 구성
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
                `
                //제목행 content 출력영역에 추가(위쪽 태그의 id 사용해야 함)
                $('#resultBox').append(str);
                // 반환 결과가 빈 array[]면
                if(result.length==0){
                    $('#prd_list').append("<tr align='center'><td colspan='7'>도서정보가 없습니다</td></tr></table>")
                }else{ //반환된 결과가 있으면, 배열이므로 결과 objects의 수만큼 반복 실행
                    for(var i=0; i < result.length; i++){ //for문 이용 api 전송데이터 한 행씩 추가
                       $('#prd_list').append('<tr><td><a class="pk" href="#">' + //tr 시작 첫번째 td인 bookno에 a태그 추가
                            result[i]['bookno'] + '</a></td><td>' +
                            result[i]['bookname'] + '</td><td>' +
                            result[i]['bookauthor'] + '</td><td>' +
                            result[i]['bookprice'] + '</td><td>' +
                            result[i]['bookdate'] + '</td><td>' +
                            result[i]['bookstock'] + '</td><td>' +
                            result[i]['pubno']['pubname'] + '</td>'+
                            '<td><button class="btn" opt="'+result[i]['bookno']+'">수정</button></td>' +
                            '<td><button class="btn2" opt="'+result[i]['bookno']+'">삭제</button></td>' +
                            '</tr>' //tr 종료
                       ) //append 종료
                    }// for 문 종료
                }//else 종료
                ('#prd_list').append('/table'); //테이블 닫음
            }, //sucess 끝
            error:function(){
                //요청 실패 후 실행할 코드
                alert("전송실패:코드확인");
            },
            complete:function(){
                //성공하던 실패하던 종료전에 정리위한 코드
                
            }
    
        });//ajax 끝
    
    });//on 끝 도서정보조회 메뉴 클릭하면 진행되는 코드의 끝
   
    ////////////////////////////////////////////////////////////////////////////////////// 
    //도서정보 조회 후 도서번호를 클릭하면 1권 도서정보를 api로 받아서 표현
    //도서번호 동적으로 생성됨, 도서번호에 클릭 이벤트 연결(도서번호는 0~n : 클래스 선택자를 이용하면 배열로 반환) 
    //이벤트 연결이 어려움
    $(document).on('click','.pk', function(){ //도서번호 a태그(클래스 pk)에 클릭이벤트 연결
        //클릭된 도서번호 추출하기
        var bookno = $(this).text(); //현재 클릭한 객체의 내부 text 추출
        alert(bookno);
        //api 요청(1권도서정보조회)
        $.ajax({
            type:"get", 
            url:"http://127.0.0.1:8000/rest_app/book/"+bookno+"/", //함수형뷰 api  url
            //url:"http://127.0.0.1:8000/rest_app/cbv/book/+bookno+"/", //클래스형뷰 api url
            datatype:'json', 
            success:function(result){
                //요청 성공 후 실행할 코드
                console.log(result); //데이터 전송되었는지 확인
                $('#index').empty(); //기존 홈 화면 지우기
                $('#resultBox').empty(); //contents 출력 영역 기존 데이터 지움
                //반환된 도서정보를 table에 표현
                const str = '<table id="prd_detail"> <tr><th>도서번호</th><td>'+result['bookno']+'</td></tr>' +
                                                    '<tr><th>도서명</th><td>'+result['bookname']+'</td></tr>' +
                                                    '<tr><th>저자</th><td>'+result['bookauthor']+'</td></tr>' +
                                                    '<tr><th>도서가격</th><td>'+result['bookprice']+'</td></tr>' +
                                                    '<tr><th>출판일</th><td>'+result['bookdate']+'</td></tr>' +
                                                    '<tr><th>재고</th><td>'+result['bookstock']+'</td></tr>' +
                                                    '<tr><th>출판사</th><td>'+result['pubno']+'</td></tr></table>' 
                $('#resultBox').append(str)

            }, //sucess 끝
            error:function(){
                //요청 실패 후 실행할 코드
                alert("전송실패:코드확인");
            },
            complete:function(){
                //성공하던 실패하던 종료전에 정리위한 코드
                
            }    
        });//ajax 끝    
    });//on 끝 도서상세보기 도서번호 클릭하면 진행되는 코드의 끝

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //// 도서정보 등록완료와 관련된 js. ajax이용 post 통신, form data json으로변경 -> api에 맞는 형식으로 전송되게 설정
    //// 도서정보 등록 완료 후 도서정보조회 메뉴로 강제 전환
    //// 도서정보 입력 후 등록버튼 클릭하면 아래 함수 진행

    $('#bkinsertform').on('submit', function(){
        //submit 이벤트 기본기능 중지
        event.preventDefault();

        //#bkinsertform form안의 data를 추출해서 json 형식으로 변경
        var formSerializeArray= $(this).serializeArray();
        console.log(formSerializeArray);
        var object={};
        for(var i=0; i<formSerializeArray.length; i++){
            object[formSerializeArray[i]['name']]=formSerializeArray[i]['value'];
        }
        console.log(object); //js객체 object를 json으로 변경
        var json = JSON.stringify(object);
        console.log(json)

        $.ajax({
            type:"post", //api의 create(insert)기능 사용
            url: "http://127.0.0.1:8000/rest_app/books/",
            data:json,//서버로 전송하는 data
            datatype:'json',//서버로부터 받을 데이터 타입
            contentType:'application/json; charset=utf-8',
            success:function(result){
                console.log(result);
                $('#index').empty();//기존화면 지움
                $('#resultBox').empty();//content출력화면 지움
                $('#list').trigger('click'); //도서정보조회메뉴 강제클릭
            },
            error:function(){
                alert("전송실패 또는 데이터입력실패")
            }
        });//ajax끝
    })//도서등록 submit on 끝

    /////////////////////////////////////////////////////////////////////////////////
    //도서정보 수정버튼 클릭 시 생성되는 수정 form구성 js founction
    //수정 버튼 동적으로 생성 : 버튼에 직접 click 이벤트 연결 불가능 -> document통해 간접 이벤트 연결
    //1) 특정도서 도서번호 추출 2) 도서번호가 포함된 api ajax 요청 3)서버로부터 전송된 도서번호의 DATA를 화면에 출력(태그포함)

    $(document).on('click','.btn', function(){
        event.preventDefault();
        //1)
        bookno = $(this).attr('opt'); //attr(속성명) : 속성의 값을 반환
        alert(bookno);
        //api 데이터 요청 : mixin기능으로 생성된 뷰에게 요청(한개 도서에 대한 데이터 요청)
        $.ajax({
            type:"get",
            url: "http://127.0.0.1:8000/rest_app/mixin/book/"+bookno+"/",
            dataType: 'json', //서버->클라이언트 datatype
            contentType: 'application/json; charset=utf-8',
            success:function(result){
                console.log(result);
                //성공했을때 전달되는 도서 한권의 정보를 수정가능하게 태그로 표현, 완료버튼 추가
                //전송할 data를 쉽게 추출하도록 form  태그 내에 표현
                $('#index').empty();
                $('#index').append("<h2>도서정보수정</h2>");
                $('#resultBox').empty();
                //데이터 표현 태그 : 태그 form 데이터 추출 -> json 변경되어야 함
                //반환된 도서정보를 table에 표현
                const str = '<form id="updateFrm"><table id="prd_detail">'+ 
                '<tr><th>도서번호</th><td><input type="text" name="bookno" value="'+result['bookno']+'"></td></tr>' +
                '<tr><th>도서명</th><td><input type="text" name="bookname" value="'+result['bookname']+'"></td></tr>' +
                '<tr><th>저자</th><td><input type="text" name="bookauthor" value="'+result['bookauthor']+'"></td></tr>' +
                '<tr><th>도서가격</th><td><input type="text" name="bookprice" value="'+result['bookprice']+'"></td></tr>' +
                '<tr><th>출판일</th><td><input type="text" name="bookdate" value="'+result['bookdate']+'"></td></tr>' +
                '<tr><th>재고</th><td><input type="text" name="bookstock" value="'+result['bookstock']+'"></td></tr>' +
                '<tr><th>출판사</th><td><input type="text" name="pubno" value="'+result['pubno'].pubno+'"></td></tr>'+ 
                '</table>' +
                '<button id="update" class="btn" opt="'+ result['bookno'] +'">완료</button>'+
                '</form>'
                $('#resultBox').append(str)

            },error:function(){
                alert("전송실패 또는 data반환 실패")
            }
        })//ajax 함수 끝
    });//도서정보수정버튼클릭 끝
    //////////////////////////////////////////////////////////////////////////////////////////
    // 도서 정보 수정 완료 기능 : 완료버튼 클릭시 실행되는 함수
    // 1. 완료버튼에 추가된 도서번호 추출 2. 수정정보 폼에서 추출 후 json으로 변경 3. api요청해서 도서 수정 ajax
    $(document).on('click','#update', function(){
        event.preventDefault();
        //1. 
        bookno = $(this).attr("opt");
        alert(bookno);

        //2.
        var formSerializeArray=$('#updateFrm').serializeArray(); //key:value 타입의 array[{name:"bookno",value:"1001"},{name:value}]
        var object = {};
        for(var i=0; i<formSerializeArray.length;i++){
            object[formSerializeArray[i]['name']]=formSerializeArray[i]['value'];//[{"bookno":"1001"}]
        }
        var json = JSON.stringify(object);
        console.log(json);
        //3.
        $.ajax({
            type:"PUT", //update 진행이므로 method가 put
            url: "http://127.0.0.1:8000/rest_app/mixin/book/"+bookno+"/",
            data:json,
            contentType:"application/json; chartset=utf-8",
            success:function(result){
                console.log(result);
                $('#index').empty();
                $('#resultBox').empty();
                $('#list').trigger('click');//도서정보조회메뉴 강세 실행
            }, 
            error:function(){
                alert("전송실패 또는 데이터오류")
            }
        });//ajax끝
    });//도서정보수정완료의 끝

////////////////////////////////////////////////////////////////////
// 도서정보 삭제
// 1. 도서번호 추출    2. 삭제할껀지 확인 메시지창 3. ajax 사용 삭제 api호출 후 도서정보조회로 이동
// api가 호출되면 바로 삭제
    $(document).on('click', '.btn2', function(){
        event.preventDefault();
        bookno = $(this).attr("opt");
        if(confirm(bookno + " 삭제하시겠습니까?")){
            //메시지에서 예(true) 선택 시 삭제 진행
            $.ajax({
                type:"DELETE",
                url:"http://127.0.0.1:8000/rest_app/mixin/book/"+bookno+"/",
                datatype:'json',
                contentType:'application/json; charset=utf-8',
                success:function(result){
                    $('#list').trigger('click');//강제로 클릭 이벤트 발생(도서정보조회 새로 요청)
                },
                error:function(){
                    alert("전송 또는 삭제 실패");
                } 
            });//ajax끝
        }//if끝
        //삭제 안하면 아무작업도 하지 않음
    });//삭제기능의 끝
});//ready 끝