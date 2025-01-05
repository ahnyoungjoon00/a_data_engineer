import { fakeApi } from "./api.js";

export default class ScatterChart {
    // 일별 사망, 부상사고 건수를 scatter chart로 작성
    transformData(datas) {
        // 월정보, 사망자수, 부상자수
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
            y: Object.values(dateInjury),
            type: 'scatter',
            mode: 'markers',
            marker: { size: 12 },
          };

          var layout = {
            title: {text: 'scatter Chart'},
            width: 1000,
            height: 500,
            xaxis: {
                title: {
                  text: '사망'
                }
              },
              yaxis: {
                title: {
                  text: '부상'
                }
              }
          };
          
          var data = [trace1];
          Plotly.newPlot('chartBox', data, layout);
    }
}