const API_key = 'yy2jqTmVG7324VL6zNamNiPfdiIQJgN/ek/aNXtsSFFfgtzCr+KAMLcesufwdWmasLUouzzgUTpQy7cMBkGurg==';
const url = 'http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath';

const accientApi = async() => {
    const paramsObj = {
        ServiceKey:API_key,
        searchYear:2023,
        sido:'',
        guGun:'',
        type:'json',
        numOfRows:10,
        pageNo:1,
    }
    const params = new URLSearchParams(paramsObj);
    // console.dir(params.toString());
    const response = await fetch(`${url}?${params.toString()}`, {method:"GET"});
    // const jsonData = await response.json();
    return await response.json();
    // console.log(jsonData);
}
const transformData = async () => {
    response = await accientApi();
    const {
        resultCode,
        items:{item},
    } = response;

    if (response.resultCode != "00"){
        throw new Error("통신 실패");
    };    
    // if(resultCode != '00'){
    //     throw new Error('통신 실패');
    // };

    // 사고년도, 발생월일시, 사망자 수, 부상자 수, 시도코드, 시군구코드, 위경도좌표
    // acc_year, occrrnc_dt, dth_dnv_cnt, injpsn_cnt, occrrnc_lc_sido_cd, occrrnc_lc_sgg_cd, lo_crd, la_crd
    const datas = item.map(e => {
        return {
            "date":e.occrrnc_dt,
            "year":e.acc_year,
            "sido":e.occrrnc_lc_sido_cd,
            "gungu":e.occrrnc_lc_sgg_cd,
            "resionCode":e.occrrnc_lc_sido_cd+e.occrrnc_lc_sgg_cd,
            deathCnt:e.dth_dnv_cnt,
            injuryCnt:e.injpsn_cnt,
            "lat":e.la_crd,
            "lot":e.lo_crd
        }
    })
    console.dir(item)
}
transformData()