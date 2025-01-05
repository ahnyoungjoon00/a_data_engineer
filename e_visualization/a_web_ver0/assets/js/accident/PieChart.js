import { fakeApi } from "./api.js";

export default class PieChart {
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

        // console.dir(monthDeath)

        return [monthDeath, monthInjury]
    }

    async drawChart() {
        document.querySelector('#chartBox').innerHTML = '';
        const datas = await fakeApi();
        const [
            monthDeath, monthInjury
        ] =this.transformData(datas);

        var trace1 = {
            labels: Object.keys(monthDeath),
            values: Object.values(monthDeath),
            type: 'pie',
            domain:{
                row:0,
                column:1
            },
          };
          
          var trace2 = {
            labels: Object.keys(monthInjury),
            values: Object.values(monthInjury),
            type: 'pie',
            domain:{
                row:0,
                column:0
            },
          };

          var layout = {
            title: {text: 'pie Chart'},
            width: 1000,
            height: 500,
          };
          
          var data = [trace1, trace2];
          Plotly.newPlot('chartBox', data, layout);
    }
}