const API_KEY = '6gGsnkx3kzFjUPZDltWFLTNtzPmIbQZG1Fck6+atY6Mqj7Oxy1l7H6d3np5jkdJAIGPuTD6D5DA74yRiZF8hIA==';
const URL = 'http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath';

const transformData = async response => { //fetch통해서 응답받은 data중 날씨데이터는 모두 포함시켜서 차트 클래스쪽으로 전달
    const {                               //차트 클래스마다 사용해야 하는 data가 다르기 때문 

    } = response;

    const datas = response.map(e => {
        return {
            'date':e.date,
            'avg_tmp':e.avg_tmp,
            'avg_cloud':e.cloud_cover,
            'high_tmp':e.high_tmp,
            'low_tmp':e.low_tmp,
            'day_rain':e.day_rain
        }
    })
    console.log(datas);
    return datas;
}

export const accidentApi = async () => {
    const paramsObj = {
        ServiceKey:API_KEY,
        searchYear:2023,
        siDo:'',
        guGun:'',
        type:'json',
        numOfRows:1,
        pageNo:1,
    }

    const params = new URLSearchParams(paramsObj);
    let response = await fetch(`${URL}?${params.toString()}`);

    const rowsCnt = await response.json();
    params.set('numOfRows', rowsCnt.totalCount)

    response = await fetch(`${URL}?${params.toString()}`);
    const jsonData = await response.json();
    return transformData(jsonData)
}

export const fakeApi = async (url) => {
    const response = await fetch(url);
    //console.log(response)
    const obj = await response.json();
    //console.log(obj)
    return transformData(obj);
}