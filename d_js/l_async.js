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

// 동기/비동기/블로킹/논블로킹
// 동기 synchronous => syn +chronous
//     윗 라인 코드의 종료시점과 아래 라인 코드의 시작시점의 시간을 맞춘다.

// 비동기 asynchronous => a + syn + chronous
//     윗 라인 코드의 종료시점과 아래 라인 코드의 시작시점의 시간을 맞추지 않는다.

// 블로킹 : 자원을 독점하고, 다른 쓰레드가 자원에 접근하는 것을 막는 것.
// 논블로킹 : 자원을 독점하지 않음

// promise
// 상태
// 1. pending       : 작업이 진행 중인 상태
// 2. fullfilled    : 작업이 성공적으로 완료된 상태
// 3. rejected      : 작업이 실패로 끝난 상태

// 후속처리메서드
// 1. then      : Promise가 fullfilled 상태일때, 실행되는
// 2. catch     : Promise가 rejected 상태일때, 실행되는
// 3. finally   : Promise의 상태와 상관없이 실행되는

const promiseCount = count => {
    return new Promise((resolve, reject) => {
        setTimeout(() =>{
            console.log(count + "초");
            resolve(count);
        }, 3000);
    });
}

// console.log(promiseCount(3));

const promiseObj = promiseCount(3)
console.log(promiseObj);

setTimeout(() => {
    console.dir(promiseObj)
}, 3100)