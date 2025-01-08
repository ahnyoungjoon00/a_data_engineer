const API_KEY = '6gGsnkx3kzFjUPZDltWFLTNtzPmIbQZG1Fck6+atY6Mqj7Oxy1l7H6d3np5jkdJAIGPuTD6D5DA74yRiZF8hIA==';
const URL = 'http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath';

const transformData = async response => {
    const {
        resultCode

    } = response;

    if(resultCode != '00'){
        throw new Error('통신 실패');
    };

    // 사고년도,  acc_year
    // 발생월일시, occrrnc_dt
    // 사망자수, dth_dnv_cnt
    // 부상자수, injpsn_cnt
    // 시도코드, occrrnc_lc_sido_cd,
    // 시군구코드, occrrnc_lc_sgg_cd
    // 경도, lo_crd
    // 위도, la_crd
    const datas = item.map(e => {
        return {
            'date':e.date,
            'avg_tmp':e.avg_tmp,
            'avg_cloud':e.avg_cloud,
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

export const fakeApi = async () => {
    const response = await fetch('http://127.0.0.1:8000/api/weather/11/');
    const obj = await response.json();
    return transformData(obj);
}