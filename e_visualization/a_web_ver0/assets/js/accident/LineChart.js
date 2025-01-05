import { fakeApi } from "./api.js";

export default class LineChart {
    transformData(datas) {
        // 월정보, 사망자수, 부상자수
        const monthAccidents = datas.map(e => {
            const month = e.date.substring(4,6) + '월';
            return {
                month: month,
                deathCnt : e.deathCnt,
                injuryCnt: e.injuryCnt,
            }
        })

        const grouped = Map.groupBy(monthAccidents, ({month}) => month);
        const monthDeath = {}
        const monthInjury = {}
        grouped.forEach((e, key) => {
            monthDeath[key] = e.reduce((acc, cur) => acc + cur.deathCnt, 0);
            monthInjury[key]  = e.reduce((acc, cur) => acc + cur.injuryCnt, 0);
        });

        console.dir(monthDeath)

        return [monthDeath, monthInjury]
    }

    async drawChart() {
        document.querySelector('#chartBox').innerHTML = '';
        const datas = await fakeApi();
        const [
            monthDeath, monthInjury
        ] =this.transformData(datas);

        var trace1 = {
            x: Object.keys(monthDeath),
            y: Object.values(monthDeath),
            type: 'scatter'
          };
          
          var trace2 = {
            x: Object.keys(monthInjury),
            y: Object.values(monthInjury),
            type: 'scatter'
          };

          var layout = {
            title: {text: 'Line Chart'},
            width: 1000,
            height: 500,
          };
          
          var data = [trace1, trace2];
          Plotly.newPlot('chartBox', data, layout);
    }
}