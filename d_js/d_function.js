// 함수 선언식

fncA()
// 함수 호이스팅 : 문제가 될 수 있어서 함수표현식을 사용하는 것을 추천
// 함수를 선언하지 않았지만 함수를 호출할 수 있음
function fncA(){
    console.log("함수");
}

function add(a, b){
    return a + b;
}
console.log("a + b =", add(10, 20));
// 함수 표현식

// fncB()
const fncB = function(){
    console.log("함수표현식");
}
console.log("============================");

// 자바스크립트의 함수는 1급객체
// 1급객체 : 값, 매개변수, 변수, 변환값
//          클로저로 사용가능
function funcObject(fnc){
    let outer1 = 2;
    let outer2 = 3;
    
    fnc()

    let innerfnc = function(){
        let inner1 = 4;
        let inner2 = 5;

        console.log("inner");
        
        return function(){
            outer1 = outer1 **2;
            console.log(outer1);
        }
    }
    return innerfnc;
}
inner = funcObject(function(){console.log("call back fnc 입니다.")});
deepInner = inner();
deepInner();
deepInner();
deepInner();

console.log("============================");
// 즉시실행함수 IIFE
// 함수를 선언함과 동시에 실행
// 선언하는 시점 딱 한번만 실행이 가능하다.
(function life(){
    let a = 100;
    console.log("즉시실행함수");
})();


// 익명함수 : function(){}
// 람다표현식
//  (arg...) => {};
// 1. 람다표현식에 매개변수가 1개라면 () 생략가능
// 2. 코드블록에 return문만 있다면 {} 생략가능

let arr =["감자", "고구마", "옥수수"];
arr.forEach(e => {
    console.log(e)
})

arr.forEach((e, idx, arr) => {
    console.log(e)
    console.log(idx, arr)
});