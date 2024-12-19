$(document).ready(function(){
$('#bkSearchFrm2').on('submit', function(){
    //bkSearchFrm 폼내에있는 submit 버튼을 클릭하면 현재 영역의 함수가 실행

    //submit의 기본 기능이 페이지 새로고침이므로 새로고침기능 막기
    event.preventDefault();

    //서버로 전송할 data 구성
    //form 태그(#bkSearchFrm2)내의 formdata(input, select의 value, hidden input : csrf)를 전송가능한 형식으로 구성
    //쿼리스트링방식으로 구성 : name=value => csrf=xxxxx&type=bookname&keyword=홍길동
    //serialize() 사용하면 자동 구성
    let formData = $(this).serialize(); //form태그 내부의 모든 input 관련 태그들을 쿼리스트링으로 묶어서 구성

    //구성한 formData를 서버에게 전달하면서 검색결과를 요청(ajax({key:value}))
    //ajax의 key는 규칙에 의해 정해져 있음
    $.ajax({
        type:"post", //form data고 method는 post로 되어 있으므로 type 설정, 생략하면 get
        url:"http://127.0.0.1:8000/book/searchres2/", //요청 url
        data:formData,//서버로 전송할 data
        datatype:'json', //여기까지가 요청정보
        success:function(result){//여기부터는 응답받은 후 처리방법을 나열, 응답후 서버로부터 전송되는 data는 result변수에 저장
            //요청 성공 후 실행할 코드
            console.log(result);
            //반환된 html 태그 정보를 div에 html 태그로 전달
            $('#searchResultBox').html(result);
        },
        error:function(){
            //요청 실패 후 실행할 코드
            alert("전송실패:코드확인");
        },
        complete:function(){
            //성공하던 실패하던 종료전에 정리위한 코드
            
        }

    });//ajax 끝

});//on 끝

});//ready 끝