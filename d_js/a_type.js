console.log('hello world!')

//자바스크립트는 타일추론을 지원하는언어
//만약 타입이 일치하지 않아 문제가 생길 경우, 컴파일러가 타입캐스팅을 알아서 진행

// 변수선언
// var 변수명 : 변수, es6 이전에 쓰던, 함수레벨 스코프변수
// let 변수명 : 변수, 
// const 변수명 : 상수(초기화 이후 값을 수정할 수 없는 변수)

// 변수 호이스팅 : 선언하기 전에 값을 쓰는 것
// 변수를 선언하지 않아도 사용할 수 있다.
console.log(vStr)
// console.log(lStr)

// 변수
// 변수 선언, 변수 할당이 나뉘어져 있음
var vStr;
vStr = 'var 변수';
let lStr = 'let 변수';
const cStr = 'const 변수';
// cStr = "a"
function studyScope(){
    if(true){
        var vScope = "var 함수레벨스코프";
        let lScope = "let 블록레벨스코프";
    }
    console.log(vScope);
};
studyScope()

// premitive type : String, Number, Boolean, Null, Undefined
// reference type : Object

// Null : 개발자가 명시적으로 해당 변수에 할당한 값이 없음을 나타내는 값
// undefined : 변수가 선언되었으나 초기화되지 않았음을 의미하는 값, 자바스크립트 엔진이 알아서 넣어줌

let username = "AYJ";
let age = 20;
let fig = true;
let empty = null;
let undefinedVal;
let obj = {name:"AYJ", age:15, info:function(){return "info"}}

console.log(username, typeof(username))
console.log(age, typeof(age))
console.log(fig, typeof(fig))
console.log(empty, typeof(empty))
console.log(undefinedVal, typeof(undefinedVal))
console.log(obj, typeof(obj))
