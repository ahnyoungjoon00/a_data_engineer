import { fakeApi } from "./api.js";

export default class LineChart {
    transformData(datas) {
        // 날짜, 평균 기온, 운량
        const data = datas.map(e => {
            const date = e.date.substring(0,10);
            return {
                date: date,
                avgTmp : e.avg_tmp,
                avgClode: e.avg_cloud,
            }
        })

        const date = {};
        const tmpData = {};
        const cloudData = {};

        grouped.forEach((e, key) => { // api data 각각 접근해서 data를 분리리
            date[key] = e.date;
            tmpData[key]  = e.avgTmp;
            cloudData[key]  = e.avgClode;
        });

        console.dir(tmpData)

        return [date, tmpData, cloudData]
    }

    async drawChart() {
        document.querySelector('#chartBox').innerHTML = '';
        const datas = await fakeApi(); // api data 요청 (비동기방식 요청 async ~ await)
        console.log(datas)
        const [
            date, tmpData, cloudData
        ] =this.transformData(datas); // 현재 클래스 transformData 사용

        var tmp = {
            x: Object.keys(tmpData),
            y: Object.values(tmpData),
            mode:"lines+markers",
            line: {
                dash:"dot",
                width:2,
                color:"red",
                shape:"spline"
            },
            name:"평균기온",
          };
          
          var cloud = {
            x: Object.keys(cloudData), // 운량의 key값(0~n)
            y: Object.values(cloudData),
            type:"bar",
            marker:{
                color:"blue",
                opacity:0.5, // 투명도
            },
            name:"평균운량량",
          };
          
          var data = [tmp, cloud];
          Plotly.newPlot('chartBox', data, layout);
    }
}