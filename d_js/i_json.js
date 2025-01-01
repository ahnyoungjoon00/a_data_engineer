// json :javascript object notation
// javascript객체 문법으로 데이터를 표현하는 문자기반 포맷
// parsing : 데이터 형식을 읽어서 프로그램에서 사용할 수 있는 구조로 변환하는 것
// serialization(직렬화) : 프로그램의 객체를 통신가능한 형태로 변화
let top1 = {
    title : '소년이 온다',
    awards : ['노벨문학상', '이상문학상', {totalCnt:2, year:[2024, 2019]}],
    category : {depth1: '문학', depth2: '소설', year:[2024, 2019]},
    'categoryCode':12,
    info:function(){
        console.log(this.title)}
}

// obj to json
const book_json = JSON.stringify(top1);
console.log(typeof book_json);
console.log(book_json);

const json_data = `{
    "acc_year": "2022",
    "occrrnc_dt": "2022010110",
    "dght_cd": "1",
    "occrrnc_day_cd": "7",
    "dth_dnv_cnt": 1,
    "injpsn_cnt": 1,
    "se_dnv_cnt": 0,
    "sl_dnv_cnt": 0,
    "wnd_dnv_cnt": 0,
    "occrrnc_lc_sido_cd": "1800",
    "occrrnc_lc_sgg_cd": "1804",
    "acc_ty_lclas_cd": "03",
    "acc_ty_mlsfc_cd": "31",
    "acc_ty_cd": "32",
    "aslt_vtr_cd": "05 ",
    "road_frm_lclas_cd": "01",
    "road_frm_cd": "02",
    "wrngdo_isrty_vhcty_lclas_cd": "01",
    "dmge_isrty_vhcty_lclas_cd": "##",
    "occrrnc_lc_x_crd": "1000059 ",
    "occrrnc_lc_y_crd": "1660526 ",
    "lo_crd": "127.50064609",
    "la_crd": "34.93956440"
}`

const obj = JSON.parse(json_data)
// console.log(typeof obj);
// console.table(obj)
// console.log(obj.sl_dnv_cnt);
console.log(">>>>>>>>>>>>>>>>>>>>>>>>>>>")

// 2. 구조분해할당
// 해석 = top1의 title 속성을 받는
const {
    title,
    category:{depth1, depth2},
    category:{depth2:dpt2},
    // == category:{depth1, depth2:dpt2},
    awards:[a, b, {totalCnt, year:[first, second]}] // 배열의 경우
} = top1;
console.log(title);
console.log(depth1);
console.log(dpt2);

console.log(a);
console.log(b);
console.log(totalCnt);

console.log(first);
console.log(second);
// console.log(top1.awards[2]["year"][0])

// top1의 수상실적년도를 first, second 변수에 담은 다음 출력.
