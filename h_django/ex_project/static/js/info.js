let toggle = 0
window.onload = function(){
    let image_btn = document.querySelector("#btn");
    image_btn.addEventListener("click", show_img);
};
// 제주도 버튼을 토글버튼으로 구성하는 js함수 구성
function show_img(){
    toggle += 1;
    let image = document.querySelector("#image")
    if (toggle%2 == 1){ // 버튼 클릭수가 홀수면 이미지 추가
    const img = new Image(); 
    img.src = src_url
    image.appendChild(img) // div태그 내에서 img 태그가 동적으로 추가됨
    }else { // 버튼 클릭수가 짝수면 이미지 제거
        image.innerHTML='';
    }
}

// function show_img(){
//     // id가 image인 div태그 표현
//     let image = document.querySelector("#image")
//     // 추가할 이미지 객체를 생성
//     const img = new Image(); // 이미지 태그 객체 생성 <img>태그
//     // 외부 스크립트 파일에 장고 탬플릿 코드가 표현하면 렌더링되지 않음
//     // img.src = "{%static 'image/제주도_ex.png'%}"
//     img.src = src_url
//     // 만들어진 img 태그를 div태그(image 변수)의 내부 요소로 삽입
//     image.appendChild(img) // div태그 내에서 img 태그가 동적으로 추가됨
// }