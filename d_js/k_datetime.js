const studyDate = () => {
    //현재 시간의 연월일시분초
    let now = new Date()
    console.log("연: ", now.getFullYear());
    console.log("월: ", now.getMonth());
    console.log("일: ", now.getDate());
    console.log("시: ", now.getHours());
    console.log("분: ", now.getMinutes());
    console.log("초: ", now.getSeconds());
    console.log("요일: ", now.getDay());
}
// studyDate()
setTimeout(() => {
    let now = new Date()
    let clock = `${now.getHours()} : ${now.getMinutes()} : ${now.getSeconds()}`;
    console.log(clock, "시작과 동시에 다음꺼 하러가고 뒤에서 따로 돌게 넘겨버림")
    setTimeout(() => {
        let now = new Date()
        let clock = `${now.getHours()} : ${now.getMinutes()} : ${now.getSeconds()}`;
        console.log(clock, "시작과 동시에 다음꺼 하러가고 뒤에서 따로 돌게 넘겨버림")

        setTimeout(() => {
            let now = new Date()
            let clock = `${now.getHours()} : ${now.getMinutes()} : ${now.getSeconds()}`;
            console.log(clock, "시작과 동시에 다음꺼 하러가고 뒤에서 따로 돌게 넘겨버림")
        },1000)
    },1000)
}, 1000)
console.log("setTimeout 함수 이후 코드, 그래서 이게 먼저 찍혀버림");

// setinertval
// setInterval(() => {
//     let now = new Date()
//     let clock = `${now.getHours()} : ${now.getMinutes()} : ${now.getSeconds()}`;
//     console.log(clock, "시작과 동시에 다음꺼 하러가고 뒤에서 따로 돌게 넘겨버림")
// }, 1000)

// setinertval
let cnt = 0;
const id = setInterval(() => {
    if(cnt > 5){
        clearInterval(id)
    }
    let now = new Date()
    let clock = `${now.getHours()} : ${now.getMinutes()} : ${now.getSeconds()}`;
    console.log(clock, "시작과 동시에 다음꺼 하러가고 뒤에서 따로 돌게 넘겨버림");
    cnt++;
}, 1000);

// setTimeout(() => {
//     clearInterval(id)
// }, 5100);