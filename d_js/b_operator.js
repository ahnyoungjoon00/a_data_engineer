// 산술 : +, -, *, /, %, **
// 문자열결합 : *
// 단항 : ++, --

// 비교 : < <= > >= == != === !==
// 논리 : &&(and) ||(or)

// 증감연산자
// ++, -- : 숫자형 변수의 앞이나 뒤에 위치, 숫자형 변수의 값을 1증가
// 전위증감연산자 : 변수 앞에 ++/--가 위치, 증감연산 수행 후 표현식 실행
// 후위증감연산자 : 변수 뒤에 ++/--가 위치, 표현식 실행 후 증감연산 실행

let nine = 9;
console.log("++nine", ++nine) // 10
console.log("nine++", nine++) // 10 출력 후, 1 증가
console.log(nine) // 11

// == 동등연산자, === 일치연산자
// 동등연산자 : 값을 비교
// 일치연산자 : 값과 타입 모두 비교

const num = 0;
const str = "0";
const arr = [];
const empty = "";
const nullVar = null;
let undefinedVar;

console.log("=================================")
console.log('0 == \'0\'', num == str)
console.log('arr == \'\'', arr == empty)

console.log('0 == \'0\'', num === str);
console.log('arr == \'\'', arr === empty);

console.log('0')
console.log('')
console.log('======================================')

// 자바스크립트 type들의 boolean 변환
// 1. false : 0, '', null, undefined, NaN
// 2. 나머지 모두 true

if(NaN){
    console.log("true")
}
else{
    console.log("false")
}