// 조건문
// if - else if - else
// switch - case

const fruit="바나나";
if(fruit==="바나나"){
    console.log("banana")
}else if(fruit === "사과"){
    console.log("apple")
}else{
    console.log("what?")
};

console.log("=================")
switch(fruit){
    case "바나나":
        console.log("switch : banana");
        break;
    case "사과" :
        console.log("switch : apple");
        break;
    default :
        console.log("what")
}

// 반복문
// while, for
console.log("=================")
// 3번 반복하는 while문 만들기
let i = 0;
while (i < 3){
    console.log("hello world!!!!!!!!!!")
    i++;
}
// 3번 반복하는 for문 만들기
for(let i = 0; i < 3; i++){
    console.log("hello world!")
}