const API_KEY = 'yy2jqTmVG7324VL6zNamNiPfdiIQJgN/ek/aNXtsSFFfgtzCr+KAMLcesufwdWmasLUouzzgUTpQy7cMBkGurg==';
const URL = 'http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath';

const transformData = async response => {
    const {
        resultCode,
        items:{item}
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
            'date':e.occrrnc_dt,
            'year':e.acc_year,
            'sido':e.occrrnc_lc_sido_cd,
            'gungo':e.occrrnc_lc_sgg_cd,
            'regionCode': e.occrrnc_lc_sido_cd + e.occrrnc_lc_sgg_cd,
            'dayOrNight': e.dght_cd == 1 ? 'day' : 'night',
            'deathCnt' : e.dth_dnv_cnt,
            'injuryCnt' : e.injpsn_cnt,
            'lat': e.la_crd,
			'lng': e.lo_crd
        }
    })

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
    const response = await fetch('assets/fakedata.json');
    const obj = await response.json();
    return transformData(obj);
}