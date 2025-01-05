import { fakeApi } from "./api.js";

export default class Histogram {
    transformData(datas) {
        // 일별 사망/부상자 건수를 scatter chart로 작성
        const dateAccidents = datas.map(e => {
            const date = e.date.substring(4,6) + '/' + e.date.substring(6,8);
            return {
                date: date,
                deathCnt : e.deathCnt,
                injuryCnt: e.injuryCnt,
            }
        })

        const grouped = Map.groupBy(dateAccidents, ({date}) => date);
        const dateDeath = {}
        const dateInjury = {}
        grouped.forEach((e, key) => {
            dateDeath[key] = e.reduce((acc, cur) => acc + cur.deathCnt, 0);
            dateInjury[key]  = e.reduce((acc, cur) => acc + cur.injuryCnt, 0);
        });

        // console.dir(dateDeath)

        return [dateDeath, dateInjury]
    }

    async drawChart() {
        document.querySelector('#chartBox').innerHTML = '';
        const datas = await fakeApi();
        const [
            dateDeath, dateInjury   
        ] =this.transformData(datas);

        var trace1 = {
          x: Object.values(dateDeath),
          type: "histogram",
          opacity: 0.5,
          marker: {
             color: 'green',
          },
        };
        var trace2 = {
          x: Object.values(dateInjury),
          type: "histogram",
          opacity: 0.6,
          marker: {
             color: 'red',
          },
          name:"injury",
        };
        
        var data = [trace1, trace2];
        var layout = {barmode: "overlay"};
        Plotly.newPlot('chartBox', data, layout);
    }
}