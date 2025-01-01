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
// quizSort()


const quizSort2 = () => {
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
        if(a.awards.length > b.awards.length){
            return -1
        }
        if(a.awards.length < b.awards.length){
            return 1
        }
        return 0
    }));
    arr.sort((a,b) => -(b.awards.length - b.awards.length))
    console.dir(arr)

}
// quizSort2()

// map
const studyMap = () => {
    let arr = [1, 2, 3, 4, 5, 6, 7];
    let res = arr.map(e => e **2);

    const ranks = [top1, top2, top3];

    let pairs = ranks.map(e => {
        return {title:e.title, category:e.category}
    })
    console.dir(pairs)
}
// studyMap()

// reduce
const studyreduce = () => {
    let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    const sum = arr.reduce((acc, cur) => {
        if (cur%2 == 0) return acc;
        // console.dir(acc)
        return acc + cur
    });
    console.log(sum);
}
// studyreduce()

const quizReduce = () => {
    // arr에 담긴 요소들의 제곱값으로 이루어진 배열을 만드시오
    // 단 reduce를 사용해서
    let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    const square = arr.reduce((acc, cur) => {
        acc.push(cur**2)
        return acc;
    }, []);
    console.dir(square);
}
// quizReduce()

// filter

const studyFilter = () => {
    let arr = [1, 2, 3, 4, 5, 6, 7];
    const res = arr.filter(e => e%2 == 0)
    console.log(res)
}
studyFilter()
