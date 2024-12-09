window.onload = function(){ // 브라우저 창이 모두 뜨고나면, 익명함수(function(){})를 실행할 것이라는 의미
    let btn = document.getElementById("btn"); // id가 btn인 태그 객체를 btn변수에 저장
    btn.addEventListener("click", show_msg); // btn객체에서 클릭이벤트가 발생하면 show_msg 함수를 실행하라
};

function show_msg(){
    alert("msg 출력"); // 확인버튼이 잇는 메시지창을 출력하게 된다.
}