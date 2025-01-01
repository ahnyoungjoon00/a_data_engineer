// 배열
// 파이썬 list

// C
// push : 배열의 가장 뒤에 요소를 추가
const studyPush = () => {
    let arr = ["a", "b", "c", "d"];
    arr.push("e");
    console.log('=======push========')
    console.log(arr)
}
studyPush()

const studyshift = () => {
    let arr = ["a", "b", "c", "d"];
    arr.unshift("e");
    console.log('==================')
    console.log(arr)
}
studyshift()

// splice : 배열에서 범위의 요소를 선택해 잘라내거나, 교체
const studysplice = () => {
    let arr = ["a", "b", "c", "d"];
    arr.splice(1, 0, "e", "f");
    console.log('==================')
    console.log(arr)
}
studysplice()

// R
const studyread = () => {
    let arr = ["a", "b", "c", "d"];
    for(let i = 0; i <arr.length; i++){
        console.log(arr[i])
    }
}
studyread()

// U
const studyupdate = () => {
    let arr = ["a", "b", "c", "d"];
    arr[3] = 999
    console.log(arr[3])

    arr.splice(2, 2, 10000, 9888)
    console.log(arr)
}
studyupdate()

// D
const studydelete = () => {
    let arr = ["a", "b", "c", "d"];
    arr[3] = undefined;
    console.log(arr);
    
    arr.splice(3, 1);
    console.log(arr);
}
studydelete()

// concat
const studyconcat = () => {
    let arr = ["a", "b", "c", "d"];
    let arr2 = ["e", "f"];
    console.log(arr.concat(arr2))
}
studyconcat()

// sort
const studysort = () => {
    let arr = ["김지윤", "hmd", "류건호", "kyt"];
    console.dir(arr.sort());

    let numArr = [10, 543, 34, 123];
    numArr.sort((a, b) => a -b);
    console.dir(numArr);
}
studysort()

const quizSort = () => {
    let top1 = {
        title : '소년이 온다',
        awards : ['노벨문학상', '이상문학상'],
        category : {depth1: '문학', depth2: '소설'},
        'categoryCode':12,
    }
    let top2 = {
        title : '당신의 이름을 지어다가 며칠은 먹었다',
        awards : [' 젊은 예술가상'],
        category : {depth1: '문학', depth2: '시'},
        'categoryCode':12,
    }
    let top3 = {
        title : 'Object',
        awards : [],
        category : {depth1: '기술', depth2: 'IT'},
        'categoryCode':15,
    }

    const arr = [top2, top3, top1]
    console.dir(arr.sort((a, b) => {
        if(a.title < b.title){
            return -1
        }
        if(a.title > b.title){
            return 1
        }
        return 0
    }));
    // 수상 개수를 기준으로 내림차순 정렬
    arr.sort((a,b) => -(b.awards.length - b.awards.length))
    console.dir(arr)
}


// map
const studyMap = () => {
    let arr = [1,2,3,4,5,6,7];
    let res = arr.map(e => e ** 2);
    const ranks = [top1, top2, top3];

    let pairs = ranks.map(e => {
        return {title:e.title, category:e.category}
    })

    console.dir(pairs)
}

// reduce
const studyReduce = () => {
    // 홀수의 합
    let arr = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9];
    const sum = arr.reduce((acc, cur) => {
        if(cur % 2 == 0) return acc;
        return acc + cur;
    });

    console.log(sum)
}

const quizReduce = () => {
    // arr에 담긴 요소들의 제곱값으로 이루어진 배열을 만드시오
    // 단 reduce를 사용해서
    let arr = [1,2,3,4,5,6,7];
    const res = arr.reduce((acc, cur) => {
        acc.push(cur**2);
        return acc
    }, [])

    console.dir(res)
}

// filter
const studyFilter = () => {
    let arr = [1,2,3,4,5,6,7];
    const res = arr.filter(e => e % 2 == 0);
    console.dir(res)
}

studyFilter()